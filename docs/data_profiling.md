# Payment Transaction Analytics System — Data Profiling Report

## 1. Objective

Perform initial exploratory data profiling of the transaction, refund, and chargeback CSV files to identify dataset structure, missing values, duplicate identifiers, status variations, and potential KPI calculation risks.

## 2. Transaction Data — `transactions.csv`

**Dataset size:** 10,000 rows × 12 columns

### Key findings

- Transaction date range: 2024-01-01 to 2024-12-30.
- Currency: INR in 9,851 rows; missing in 149 rows.
- Duplicate transaction IDs: 267.
- Missing transaction IDs: 151.
- Missing transaction amounts: 202.
- Missing transaction dates: 151.

### Normalized transaction statuses

| Status | Row Count |
|---|---:|
| Success | 8,117 |
| Failed | 1,163 |
| Pending | 571 |
| Missing | 149 |
| Total | 10,000 |

Status values were normalized in memory by trimming whitespace and converting text to lowercase. The original CSV was not modified.

## 3. Refund Data — `refunds.csv`

**Dataset size:** 10,000 rows

### Refund status counts

| Status | Row Count |
|---|---:|
| Completed | 6,951 |
| Pending | 1,934 |
| Rejected | 967 |
| Missing | 148 |
| Total | 10,000 |

### Key findings

- Duplicate refund IDs: 263.
- Missing refund IDs: 148.
- Missing transaction IDs: 198.
- Missing refund amounts: 147.
- Missing refund dates: 149.
- Missing refund statuses: 148.

Refund amount calculations require an agreed rule for which refund statuses qualify.

## 4. Chargeback Data — `chargebacks.csv`

**Dataset size:** 10,000 rows

### Chargeback status counts

| Status | Row Count |
|---|---:|
| Open | 2,982 |
| Won | 2,490 |
| Under Review | 2,430 |
| Lost | 1,953 |
| Missing | 145 |
| Total | 10,000 |

### Key findings

- Duplicate chargeback IDs: 265.
- Missing chargeback IDs: 149.
- Missing transaction IDs: 201.
- Missing chargeback amounts: 246.
- Missing chargeback dates: 153.
- Missing chargeback statuses: 145.

Chargeback amount calculations require an agreed rule for whether all statuses or only selected statuses should be included.

## 5. Data Quality Risks

1. Missing identifiers may prevent reliable unique-record counting and joining.
2. Duplicate identifiers may inflate counts and monetary totals.
3. Missing amounts may affect transaction, refund, and chargeback totals.
4. Inconsistent transaction status formatting may cause incorrect classifications if exact text matching is used.
5. Missing dates may affect daily, weekly, and monthly trend analysis.
6. Missing currency values require review before monetary totals are finalized.
7. Missing customer, merchant, and payment method identifiers may affect relationship-based analysis.

## 6. Recommended Actions

- Preserve all original files in `data/raw/`.
- Perform cleaning and normalization only in memory or in approved processed-data locations.
- Validate identifier uniqueness and relationships before aggregation.
- Confirm transaction success and failure classification rules.
- Confirm the treatment of pending and missing transaction statuses.
- Confirm which refund and chargeback statuses qualify for their amount KPIs.
- Validate KPI totals against the original source files.

## 7. Scope and Limitations

This report records preliminary profiling results for Day-1 dashboard requirements. It does not perform permanent data cleaning, establish final business rules, or implement the production Power BI dashboard.

The results must be reviewed before being used as final business metrics.