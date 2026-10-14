# Payment Transaction Analysis System — KPI Definitions

**Jira Task:** SCRUM-15 — Day 1: Dashboard Requirements & Wireframe

## 1. Purpose

This document defines the business meaning, calculation requirements, source files, required fields, expected business use, and recommended visuals for the nine KPIs required on the Executive Overview dashboard.

The calculations below are initial specifications. Transaction status mappings, currency handling, and refund/chargeback inclusion rules must be validated against the source data before implementation.

## 2. KPI Definitions

### KPI 1 — Total Transactions

**Business Definition:**  
Total number of distinct payment transactions recorded in the transaction dataset.

**Calculation:**  
Count distinct `transaction_id`.

**Required CSV:**  
`data/raw/transactions.csv`

**Required Fields:**
- `transaction_id`

**Expected Business Use:**
- Monitor overall transaction activity.
- Compare transaction volume across reporting periods.
- Identify periods of unusually high or low activity.

**Recommended Visual:**  
KPI Card.

**Validation Notes:**  
Check for null and duplicate transaction IDs before confirming the final calculation.

---

### KPI 2 — Total Transaction Value

**Business Definition:**  
Total monetary value of the recorded payment transactions.

**Calculation:**  
Sum `amount` for the transactions included in the reporting scope.

**Required CSV:**  
`data/raw/transactions.csv`

**Required Fields:**
- `transaction_id`
- `amount`
- `currency`

**Expected Business Use:**
- Monitor the overall monetary value processed.
- Compare transaction value across periods, payment methods, providers, and merchants.
- Identify changes in payment activity.

**Recommended Visual:**
- KPI Card
- Transaction value trend line chart

**Validation Notes:**  
Confirm whether the dataset contains multiple currencies. If it does, amounts must not be added together as though they share one currency unless an agreed currency-conversion method is applied. Document whether the KPI includes all transaction statuses or only selected statuses.

---

### KPI 3 — Average Transaction Amount

**Business Definition:**  
Average monetary amount per included transaction.

**Calculation:**  
Sum of included transaction amounts divided by the count of included transactions with valid amounts.

Alternatively, use the average of `amount` after confirming the inclusion and missing-value rules.

**Required CSV:**  
`data/raw/transactions.csv`

**Required Fields:**
- `transaction_id`
- `amount`
- `currency`

**Expected Business Use:**
- Understand the typical transaction size.
- Compare average transaction amounts across payment methods, channels, customers, and merchants.
- Identify changes in transaction behavior.

**Recommended Visual:**
- KPI Card
- Bar chart for segment comparisons

**Validation Notes:**  
Confirm the transaction inclusion rules and currency handling. The amount denominator should include only transactions with valid amounts.

---

### KPI 4 — Successful Transactions

**Business Definition:**  
Number of transactions whose status represents a successful payment outcome.

**Calculation:**  
Count distinct `transaction_id` where `transaction_status` belongs to the approved successful-status mapping.

**Required CSV:**  
`data/raw/transactions.csv`

**Required Fields:**
- `transaction_id`
- `transaction_status`

**Expected Business Use:**
- Monitor successful payment activity.
- Compare successful transaction counts over time.
- Evaluate outcomes by payment method, provider, channel, and location.

**Recommended Visual:**
- KPI Card
- Success/failure comparison chart

**Validation Notes:**  
Inspect the actual distinct values of `transaction_status` and agree on the successful-status mapping before implementation. Do not assume a status value without validation.

---

### KPI 5 — Failed Transactions

**Business Definition:**  
Number of transactions whose status represents a failed payment outcome.

**Calculation:**  
Count distinct `transaction_id` where `transaction_status` belongs to the approved failed-status mapping.

**Required CSV:**  
`data/raw/transactions.csv`

**Required Fields:**
- `transaction_id`
- `transaction_status`

**Expected Business Use:**
- Monitor payment failures.
- Identify periods with elevated failure activity.
- Investigate differences in failure counts across payment methods, providers, channels, and locations.

**Recommended Visual:**
- KPI Card
- Success/failure comparison chart
- Failure trend line chart

**Validation Notes:**  
Confirm the failed-status mapping from the actual source data. Pending, cancelled, reversed, or other statuses should not automatically be classified as failed without an agreed business rule.

---

### KPI 6 — Success Rate

**Business Definition:**  
Percentage of eligible transactions classified as successful.

**Calculation:**  

Success Rate = Successful Transactions ÷ Eligible Transactions × 100

**Required CSV:**  
`data/raw/transactions.csv`

**Required Fields:**
- `transaction_id`
- `transaction_status`

**Expected Business Use:**
- Evaluate payment processing performance.
- Compare success rates across payment methods, providers, channels, and time periods.
- Identify segments requiring investigation.

**Recommended Visual:**
- KPI Card
- Trend line chart
- Payment method comparison chart

**Validation Notes:**  
Define eligible transactions consistently. Exclude statuses such as pending or cancelled from the denominator only if the approved business rule requires it. Handle a zero denominator by returning blank or not applicable rather than dividing by zero.

---

### KPI 7 — Failure Rate

**Business Definition:**  
Percentage of eligible transactions classified as failed.

**Calculation:**  

Failure Rate = Failed Transactions ÷ Eligible Transactions × 100

**Required CSV:**  
`data/raw/transactions.csv`

**Required Fields:**
- `transaction_id`
- `transaction_status`

**Expected Business Use:**
- Monitor payment reliability.
- Identify periods with elevated failure activity.
- Compare failure rates across payment methods, providers, channels, and locations.

**Recommended Visual:**
- KPI Card
- Trend line chart
- Failure comparison bar chart

**Validation Notes:**  
Use the same eligible-transaction denominator as the Success Rate KPI. Success Rate plus Failure Rate may be less than 100% when other eligible-status categories are handled separately; the final rule must be documented.

---

### KPI 8 — Total Refund Amount

**Business Definition:**  
Total monetary amount represented by refund records included under the agreed refund-status rules.

**Calculation:**  
Sum `refund_amount` for refund records included in the reporting scope.

**Required CSV:**  
`data/raw/refunds.csv`

**Required Fields:**
- `refund_id`
- `transaction_id`
- `refund_date`
- `refund_amount`
- `refund_status`

**Expected Business Use:**
- Monitor refund exposure.
- Compare refund amounts across periods.
- Investigate refund patterns by customer, merchant, and original transaction.

**Recommended Visual:**
- KPI Card
- Refund amount trend line chart
- Refund analysis table

**Validation Notes:**  
Confirm which refund statuses should be included, such as completed refunds versus pending or rejected refunds. Avoid duplicating refund amounts when relating refund records to transaction records. Confirm currency treatment before aggregation.

---

### KPI 9 — Total Chargeback Amount

**Business Definition:**  
Total monetary amount represented by chargeback records included under the agreed chargeback-status rules.

**Calculation:**  
Sum `chargeback_amount` for chargeback records included in the reporting scope.

**Required CSV:**  
`data/raw/chargebacks.csv`

**Required Fields:**
- `chargeback_id`
- `transaction_id`
- `chargeback_date`
- `chargeback_amount`
- `chargeback_status`

**Expected Business Use:**
- Monitor chargeback exposure.
- Identify changes in chargeback amounts over time.
- Investigate patterns by merchant, customer, and original transaction.

**Recommended Visual:**
- KPI Card
- Chargeback amount trend line chart
- Chargeback analysis table

**Validation Notes:**  
Confirm which chargeback statuses should be included. Avoid duplicating chargeback amounts when joining to transaction records. Confirm currency treatment before aggregation.

---

## 3. KPI Summary

| KPI Name | Primary Source | Recommended Visual |
|---|---|---|
| Total Transactions | `transactions.csv` | KPI Card |
| Total Transaction Value | `transactions.csv` | KPI Card and line chart |
| Average Transaction Amount | `transactions.csv` | KPI Card |
| Successful Transactions | `transactions.csv` | KPI Card and comparison chart |
| Failed Transactions | `transactions.csv` | KPI Card and comparison chart |
| Success Rate | `transactions.csv` | KPI Card and trend chart |
| Failure Rate | `transactions.csv` | KPI Card and trend chart |
| Total Refund Amount | `refunds.csv` | KPI Card and line chart |
| Total Chargeback Amount | `chargebacks.csv` | KPI Card and line chart |

## 4. Shared Calculation Rules to Confirm

Before implementing these KPIs in Power BI:

1. Validate uniqueness and completeness of transaction IDs.
2. Inspect actual transaction status values and document successful, failed, and excluded categories.
3. Agree on the transaction inclusion rules and use consistent denominators for success and failure rates.
4. Confirm currency handling for transaction, refund, and chargeback amounts.
5. Confirm which refund and chargeback statuses qualify for their respective amount KPIs.
6. Avoid double-counting transaction amounts when joining to refund or chargeback records.
7. Test KPI totals against the original CSV files without modifying the raw data.

## 5. Day-1 Scope

This document specifies KPI requirements and calculation assumptions. Actual KPI implementation, production DAX measures, and the final Power BI dashboard are outside the scope of Day-1 task SCRUM-15.