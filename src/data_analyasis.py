from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

from pathlib import Path

DOCS_DIR = Path(__file__).resolve().parent.parent / "docs"
DOCS_DIR.mkdir(parents=True, exist_ok=True)


df=pd.read_csv("data/raw/transactions.csv")

PROJECT_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = PROJECT_DIR / "data" / "raw"
DOCS_DIR = PROJECT_DIR / "docs"
SRC_DIR = PROJECT_DIR / "src"

DOCS_DIR.mkdir(parents=True, exist_ok=True)

# Load transactions and customer/merchant  information.
transactions = pd.read_csv(DATA_DIR / "transactions.csv")
customers = pd.read_csv(DATA_DIR / "customers.csv")
merchants = pd.read_csv(DATA_DIR / "merchants.csv")


print("\nCustomer Transaction Analysis:")
print(customers.head(10).to_string(index=False))

print("\nTotal customers in transaction data:")
print(customers.shape[0])

#  grouping and joining.
for data, required, filename in [
    (transactions, ["transaction_id", "customer_id", "merchant_id", "amount"],
     "transactions.csv"),
    (customers, ["customer_id"], "customers.csv"),
    (merchants, ["merchant_id"], "merchants.csv")
]:
    missing = [col for col in required if col not in data.columns]
    if missing:
        raise ValueError(f"{filename} missing {missing}; available: {list(data.columns)}")

# Convert transaction amounts to numeric.
transactions["amount"] = pd.to_numeric(transactions["amount"], errors="coerce")

# Aggregate transactions by customer.
customer_stats = transactions.groupby("customer_id", dropna=False).agg(
    transaction_count=("transaction_id", "count"),
    total_amount=("amount", "sum"),
    average_amount=("amount", "mean")
).reset_index()

# Sort highest total spending first.
customer_stats = customer_stats.sort_values(
    "total_amount", ascending=False
)

# Sort highest total spending first.
customer_stats = customer_stats.sort_values(
    "total_amount", ascending=False
)

# Attach customer details without dropping unmatched customer IDs.
customer_report = customer_stats.merge(
    customers.drop_duplicates("customer_id"),
    on="customer_id", how="left"
)
customer_report.to_csv(
    DOCS_DIR / "customer_spending_ranking.csv", index=False
)

# Aggregate transactions by merchant.
merchant_stats = transactions.groupby("merchant_id", dropna=False).agg(
    transaction_count=("transaction_id", "count"),
    total_amount=("amount", "sum"),
    average_amount=("amount", "mean")
).reset_index()

# Rank merchants by transaction count, highest first.
merchant_stats = merchant_stats.sort_values(
    "transaction_count", ascending=False
)
# Attach merchant attributes for business interpretation.
merchant_report = merchant_stats.merge(
    merchants.drop_duplicates("merchant_id"),
    on="merchant_id", how="left"
)
merchant_report.to_csv(
    DOCS_DIR / "merchant_volume_ranking.csv", index=False
)

# If merchant category exists, compare activity by category.
if "category" in merchant_report.columns:
    category_report = merchant_report.groupby("category", dropna=False).agg(
        merchant_count=("merchant_id", "nunique"),
        transaction_count=("transaction_count", "sum"),
        total_amount=("total_amount", "sum")
    ).reset_index()

    category_report.to_csv(
        DOCS_DIR / "merchant_category_analysis.csv", index=False
    )

# Customer KPIs
customer_kpis = transactions.groupby("customer_id").agg(
    transaction_count=("transaction_id", "count"),
    total_amount=("amount", "sum"),
    average_amount=("amount", "mean")
).reset_index()

customer_kpis.to_csv(DOCS_DIR / "customer_kpis.csv", index=False)

# Merchant KPIs
merchant_kpis = transactions.groupby("merchant_id").agg(
    transaction_count=("transaction_id", "count"),
    total_amount=("amount", "sum"),
    average_amount=("amount", "mean")
).reset_index()

merchant_kpis.to_csv(DOCS_DIR / "merchant_kpis.csv", index=False)

# Failed Transactions
failed = transactions[
    transactions["transaction_status"].astype(str).str.strip().str.lower()
    == "failed"
]
failed.to_csv(DOCS_DIR / "failed_transactions.csv", index=False)

# Monthly Trends
transactions["transaction_date"] = pd.to_datetime(
    transactions["transaction_date"], errors="coerce"
)
transactions["month"] = transactions["transaction_date"].dt.to_period("M")

monthly = transactions.groupby("month").agg(
    transaction_count=("transaction_id", "count"),
    total_amount=("amount", "sum")
).reset_index()

monthly.to_csv(DOCS_DIR / "monthly_trends.csv", index=False)

print("All analysis files created successfully!")
print("Review customer and merchant rankings in docs/.")

