import pandas as pd

from src.analysis.common import (
    load_project_csv,
    require_columns,
)


class PaymentMethodAnalyzer:
    """Analyze payment method usage, transaction performance, and data quality."""

    PAYMENT_METHOD_COLUMNS = [
        "payment_method_id",
        "method_type",
        "provider",
        "is_default",
    ]

    TRANSACTION_COLUMNS = [
        "transaction_id",
        "payment_method_id",
        "amount",
        "transaction_status",
    ]

    STATUS_MAPPING = {
        "success": "Success",
        "failed": "Failed",
        "pending": "Pending",
    }

    def __init__(
        self,
        payment_methods_file="payment_methods.csv",
        transactions_file="transactions.csv",
    ):
        self.payment_methods_file = payment_methods_file
        self.transactions_file = transactions_file

        self.payment_methods = None
        self.transactions = None
        self.payment_methods_clean = None
        self.analysis_data = None
        self.conflicting_payment_method_ids = []

    def load_data(self):
        """Load and validate the source CSV files."""

        self.payment_methods = load_project_csv(
            self.payment_methods_file
        )
        self.transactions = load_project_csv(
            self.transactions_file
        )

        require_columns(
            self.payment_methods,
            self.PAYMENT_METHOD_COLUMNS,
            self.payment_methods_file,
        )
        require_columns(
            self.transactions,
            self.TRANSACTION_COLUMNS,
            self.transactions_file,
        )

        return {
            "payment_methods_shape": self.payment_methods.shape,
            "transactions_shape": self.transactions.shape,
        }

    def prepare_data(self):
        """Standardize analysis fields without changing raw CSV files."""

        if self.payment_methods is None or self.transactions is None:
            raise RuntimeError("Call load_data() before prepare_data().")

        methods = self.payment_methods.copy()
        transactions = self.transactions.copy()

        # Standardize boolean-like values in the analysis copy.
        methods["is_default"] = (
            methods["is_default"]
            .astype("string")
            .str.strip()
            .str.lower()
            .replace({"1": "true", "0": "false"})
        )

        # Remove fully identical rows after standardization.
        methods = methods.drop_duplicates().copy()

        # Identify IDs with conflicting records before resolving join keys.
        duplicate_methods = methods[
            methods["payment_method_id"].notna()
            & methods["payment_method_id"].duplicated(keep=False)
        ]

        self.conflicting_payment_method_ids = (
            duplicate_methods.loc[
                duplicate_methods.groupby("payment_method_id")[
                    "payment_method_id"
                ].transform("size") > 1,
                "payment_method_id",
            ]
            .drop_duplicates()
            .tolist()
        )

        # Use the first source record per ID for the join.
        # Conflicting IDs are reported in the data quality summary.
        self.payment_methods_clean = (
            methods.dropna(subset=["payment_method_id"])
            .drop_duplicates(
                subset=["payment_method_id"],
                keep="first",
            )
            .copy()
        )

        # Standardize transaction statuses in the analysis copy.
        status = (
            transactions["transaction_status"]
            .astype("string")
            .str.strip()
            .str.lower()
        )

        transactions["normalized_status"] = (
            status.map(self.STATUS_MAPPING).fillna("Unknown")
        )

        transactions["amount"] = pd.to_numeric(
            transactions["amount"],
            errors="coerce",
        )

        self.transactions = transactions

    def merge_data(self):
        """Join transactions to the unique payment method records."""

        if self.payment_methods is None or self.transactions is None:
            raise RuntimeError("Call load_data() before merge_data().")

        self.prepare_data()

        self.analysis_data = self.transactions.merge(
            self.payment_methods_clean,
            on="payment_method_id",
            how="left",
            suffixes=("_transaction", "_method"),
            validate="many_to_one",
            indicator=True,
        )

        return self.analysis_data

    def check_data_quality(self):
        """Return key data quality observations."""

        if self.payment_methods is None or self.transactions is None:
            raise RuntimeError(
                "Call load_data() before check_data_quality()."
            )

        if self.analysis_data is None:
            self.merge_data()

        checks = {
            "Payment method source rows": len(self.payment_methods),
            "Transaction rows": len(self.transactions),
            "Exact duplicate payment method rows in source":
                int(self.payment_methods.duplicated().sum()),
            "Missing payment method IDs in source":
                int(self.payment_methods["payment_method_id"].isna().sum()),
            "Conflicting payment method IDs":
                len(self.conflicting_payment_method_ids),
            "Transactions with missing payment method ID":
                int(self.transactions["payment_method_id"].isna().sum()),
            "Unmatched transaction rows":
                int((self.analysis_data["_merge"] == "left_only").sum()),
            "Transactions with unknown status":
                int((self.transactions["normalized_status"] == "Unknown").sum()),
        }

        return pd.DataFrame(
            list(checks.items()),
            columns=["Data quality check", "Count"],
        )

    def _build_summary(self, group_columns):
        """Build reusable transaction metrics for selected dimensions."""

        if self.analysis_data is None:
            self.merge_data()

        data = self.analysis_data.copy()
        data[group_columns] = data[group_columns].fillna("Unknown")

        summary = (
            data.groupby(group_columns, dropna=False)
            .agg(
                transaction_count=("transaction_id", "size"),
                total_amount=("amount", "sum"),
                average_amount=("amount", "mean"),
                success_count=(
                    "normalized_status",
                    lambda values: values.eq("Success").sum(),
                ),
                failure_count=(
                    "normalized_status",
                    lambda values: values.eq("Failed").sum(),
                ),
            )
            .reset_index()
        )

        # Rates use all transaction rows in each group as the denominator.
        summary["success_rate_pct"] = (
            summary["success_count"]
            / summary["transaction_count"]
            * 100
        ).round(2)

        summary["failure_rate_pct"] = (
            summary["failure_count"]
            / summary["transaction_count"]
            * 100
        ).round(2)

        return summary

    def payment_method_summary(self):
        """Summarize metrics by payment method type and provider."""

        return self._build_summary(["method_type", "provider"])

    def provider_summary(self):
        """Compare transaction performance by provider."""

        return self._build_summary(["provider"])