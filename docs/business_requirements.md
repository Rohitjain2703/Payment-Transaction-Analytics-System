# Payment Transaction Analysis System — Dashboard Business Requirements

## 1. Document Purpose

This document defines the business requirements for the Payment Transaction Analysis System dashboard. It identifies the target users, dashboard pages, KPIs, visuals, filters, business questions, navigation, and initial implementation recommendations before production dashboard development begins.

**Jira:** SCRUM-15 — Day 1: Dashboard Requirements & Wireframe

**Scope:** Requirements and wireframe preparation only. The final Power BI dashboard is not part of Day 1.

## 2. Dashboard Objective

Provide a business-focused view of payment transaction performance, transaction volume and value, successful and failed transactions, payment methods and providers, customer activity, merchant performance, refunds, chargebacks, geographic patterns, and time trends.

The dashboard should help stakeholders monitor performance, identify unusual patterns, compare business segments, and determine areas requiring further investigation.

## 3. Source Data

Primary source:
- `data/raw/transactions.csv`

Supporting sources:
- `data/raw/customers.csv`
- `data/raw/merchants.csv`
- `data/raw/payment_methods.csv`
- `data/raw/refunds.csv`
- `data/raw/chargebacks.csv`

The original CSV files are read-only source data for this task. They must not be edited, renamed, deleted, or overwritten.

## 4. Target Users

| Target user | Requirements |
|---|---|
| Business stakeholders | Monitor transaction performance, payment outcomes, refunds, chargebacks, and trends. |
| Management | Review high-level KPIs, business performance, and important exceptions. |
| Data Analysts | Explore transactions by date, status, payment method, customer, merchant, and location. |
| Data Scientists | Identify patterns and segments that may warrant deeper analysis. |
| Project Team | Validate business definitions, source fields, calculations, and dashboard requirements. |

## 5. Dashboard Page Structure

### Page 1 — Executive Overview

**Purpose:** Provide a high-level view of overall payment transaction performance.

**Required KPI cards:**
- Total Transactions
- Total Transaction Value
- Average Transaction Amount
- Successful Transactions
- Failed Transactions
- Success Rate
- Failure Rate
- Total Refund Amount
- Total Chargeback Amount

**Recommended visuals:**
- Transaction volume trend
- Transaction value trend
- Successful versus failed transaction comparison
- Transaction status distribution
- Top-level business summary

**Proposed layout:**
1. Page title and global filters at the top.
2. KPI cards arranged in two rows if necessary.
3. Transaction volume and transaction value trends in the middle.
4. Success/failure comparison and status distribution below.
5. A short business summary at the bottom.

### Page 2 — Transactions & Payment Methods

**Purpose:** Analyze transaction performance and payment method behavior.

**Required analysis:**
- Transaction volume and value
- Average transaction amount
- Transaction status and type
- Payment method and provider
- Transaction channel

**Recommended visuals:**
- Transaction trend
- Transaction volume by payment method
- Transaction value by payment method
- Success/failure by payment method
- Provider comparison
- Transaction type comparison
- Channel comparison

**Required slicers:**
- Date
- Transaction Status
- Transaction Type
- Payment Method
- Provider
- Channel

**Proposed layout:**
1. Page title and slicers at the top.
2. Transaction volume, value, and average amount KPI cards.
3. Transaction trend across the page.
4. Payment method and provider comparisons in the middle.
5. Status, transaction type, and channel comparisons at the bottom.

### Page 3 — Customer & Merchant

**Purpose:** Analyze customer activity and merchant performance.

**Customer requirements:**
- Customer transaction count
- Customer transaction value
- Average customer transaction amount
- Top customers by transaction value
- Top customers by transaction count
- Customer type and location

**Merchant requirements:**
- Merchant transaction count
- Merchant transaction value
- Average merchant transaction amount
- Top merchants by transaction value
- Top merchants by transaction count
- Merchant category, type, and location

**Recommended visuals:**
- Top customers by transaction value
- Top customers by transaction count
- Top merchants by transaction value
- Top merchants by transaction count
- Customer type comparison
- Merchant category comparison
- Customer and merchant location analysis

**Proposed layout:**
1. Page title and applicable global filters at the top.
2. Customer and merchant KPI groups.
3. Customer rankings in one section and merchant rankings in another.
4. Customer type and merchant category comparisons.
5. Location analysis at the bottom.

### Page 4 — Location & Trends

**Purpose:** Analyze geographic and time-based transaction patterns.

**Required analysis:**
- Daily transaction trend
- Weekly and monthly transaction trend
- Transaction value trend
- Success/failure trend
- City and state performance
- Transaction value by location
- Transaction volume by location

**Recommended visuals:**
- Time-series line charts
- City and state bar charts
- Map visual where appropriate
- Success/failure trend
- Transaction value trend

**Required slicers:**
- Date
- City
- State
- Transaction Status
- Transaction Type
- Channel

**Proposed layout:**
1. Page title and location/time slicers at the top.
2. Transaction volume and value trend charts.
3. Success/failure trend.
4. City and state comparison charts.
5. Map visual where geographic fields and mapping support are suitable.

## 6. Global Filters and Slicers

The following filters should be considered for dashboard-wide use:

- Transaction Date
- Transaction Status
- Transaction Type
- Payment Method
- Payment Provider
- Channel
- Customer
- Customer Type
- Merchant
- Merchant Category
- Merchant Type
- City
- State

The final scope of each global filter must be confirmed against the four page designs and the available source fields.

## 7. KPI Requirements

The dashboard requirements include the following KPIs:

| KPI | Business definition | Initial calculation requirement | Main source |
|---|---|---|---|
| Total Transactions | Number of payment transaction records | Count distinct `transaction_id` | `transactions.csv` |
| Total Transaction Value | Sum of transaction amounts | Sum of `amount`, subject to currency handling | `transactions.csv` |
| Average Transaction Amount | Average amount per transaction | Transaction amount divided by transaction count, or average of transaction amounts under the agreed inclusion rules | `transactions.csv` |
| Successful Transactions | Transactions classified as successful | Count transactions whose status is mapped to successful | `transactions.csv` |
| Failed Transactions | Transactions classified as failed | Count transactions whose status is mapped to failed | `transactions.csv` |
| Success Rate | Share of transactions classified as successful | Successful transactions divided by eligible transactions | `transactions.csv` |
| Failure Rate | Share of transactions classified as failed | Failed transactions divided by eligible transactions | `transactions.csv` |
| Total Refund Amount | Amount refunded | Sum `refund_amount`, with refund-status rules agreed | `refunds.csv` |
| Total Chargeback Amount | Amount charged back | Sum `chargeback_amount`, with chargeback-status rules agreed | `chargebacks.csv` |

Detailed KPI definitions, field mappings, and calculation assumptions should be maintained in `docs/kpi_definitions.md`.

## 8. Data Field Mapping

| Dashboard requirement | Source field mapping |
|---|---|
| Transaction ID | `transactions.csv` → `transaction_id` |
| Transaction Amount | `transactions.csv` → `amount` |
| Transaction Date | `transactions.csv` → `transaction_date` |
| Transaction Status | `transactions.csv` → `transaction_status` |
| Transaction Type | `transactions.csv` → `transaction_type` |
| Transaction Channel | `transactions.csv` → `channel` |
| Transaction Location | `transactions.csv` → `city`, `state` |
| Customer | `transactions.csv` → `customer_id`; `customers.csv` → `customer_id`, `customer_name` |
| Customer Type | `customers.csv` → `customer_type` |
| Customer Location | `customers.csv` → `city`, `state` |
| Merchant | `transactions.csv` → `merchant_id`; `merchants.csv` → `merchant_id`, `merchant_name` |
| Merchant Category | `merchants.csv` → `category` |
| Merchant Type | `merchants.csv` → `merchant_type` |
| Merchant Location | `merchants.csv` → `city`, `state` |
| Payment Method | `transactions.csv` → `payment_method_id`; `payment_methods.csv` → `payment_method_id`, `method_type` |
| Payment Provider | `payment_methods.csv` → `provider` |
| Refund Amount | `refunds.csv` → `refund_amount` |
| Refund Status | `refunds.csv` → `refund_status` |
| Chargeback Amount | `chargebacks.csv` → `chargeback_amount` |
| Chargeback Status | `chargebacks.csv` → `chargeback_status` |

The mapping is based on the documented data dictionary. Field availability and join behavior should be validated before implementation.

## 9. Business Questions

The dashboard should help answer:

1. What is the total transaction volume?
2. What is the total transaction value?
3. What is the transaction success rate?
4. How are transactions trending over time?
5. Which payment methods perform best?
6. Which payment providers perform best?
7. Which customers generate the highest transaction value?
8. Which merchants generate the highest transaction value?
9. Which cities and states have the highest transaction activity?
10. What are the refund and chargeback levels?
11. Which transaction periods have high failure activity?
12. Which areas require further business investigation?

## 10. Dashboard Design Recommendations

- Maintain a consistent title, filter area, KPI placement, and page navigation across pages.
- Place the most important KPIs near the top of each page.
- Use line charts for trends and bar charts for category comparisons.
- Use tables for detailed customer and merchant rankings where appropriate.
- Add tooltips for supporting information without overcrowding visuals.
- Provide drill-down from higher-level time or geographic views where the underlying fields support it.
- Keep slicers easy to find and ensure their intended page/global scope is documented.
- Provide consistent page navigation between all four pages.
- Validate cross-filtering, slicer interactions, and date behavior during implementation.
- Choose final colors and themes after requirements and layout have been reviewed.

## 11. Navigation Requirements

Provide navigation between:
1. Executive Overview
2. Transactions & Payment Methods
3. Customer & Merchant
4. Location & Trends

A consistent navigation bar or page-navigation buttons should allow users to move between the four pages. Navigation behavior should be tested during implementation.

## 12. Initial Power BI Implementation Recommendations

- Import the source CSV files without changing the originals.
- Define and validate relationships using the documented identifiers.
- Consider a dedicated date table for daily, weekly, and monthly reporting.
- Define reusable measures for transaction counts, transaction value, average amount, success/failure counts and rates, refunds, and chargebacks.
- Document the status values included in successful and failed transaction calculations.
- Confirm currency handling before aggregating amounts across currencies.
- Prevent duplicated transaction amounts when joining one-to-many refund or chargeback records.
- Validate totals and filters against the source datasets before release.
- Keep production dashboard development outside the scope of this Day-1 task.

## 13. Open Questions and Assumptions

The following items require validation or stakeholder confirmation:

- Which `transaction_status` values count as successful, failed, pending, or otherwise excluded?
- Can transaction amounts contain multiple currencies, and should totals be displayed separately by currency?
- Should refunds and chargebacks include all statuses or only selected statuses?
- Should transaction counts include every record or only distinct transaction IDs after data-quality checks?
- Which date should drive refund and chargeback trends: the event date or original transaction date?
- Should customer/merchant location visuals use transaction location, customer location, or merchant location?
- Which global slicers should apply to all pages versus individual pages?
- Are there agreed rules for excluding test, reversed, or cancelled transactions?

These questions must be resolved or documented as assumptions before production implementation.

## 14. Day-1 Scope and Deliverables

Day-1 deliverables:
- Dashboard objective and target users
- Four-page dashboard structure
- KPI requirements and calculation assumptions
- Source field mapping
- Visual and slicer requirements
- Business questions
- Dashboard design and navigation recommendations
- Four-page dashboard wireframe
- Open questions and blockers

The final production Power BI dashboard is explicitly out of scope for Day 1.