# Payment Transaction Analytics System — Dashboard Wireframe

## 1. Purpose

This document defines the proposed layout and navigation for the four Power BI dashboard pages required by Jira task SCRUM-15.

This is a Day-1 planning wireframe, not the final production dashboard.

## 2. Common Page Layout

All four pages will follow a consistent structure.

```text
+------------------------------------------------------------------+
| DASHBOARD TITLE                         Last Refresh / Info       |
+------------------------------------------------------------------+
| PAGE NAVIGATION: Overview | Transactions | Customer & Merchant   |
|                  Location & Trends                                |
+------------------------------------------------------------------+
| GLOBAL FILTERS / PAGE-SPECIFIC SLICERS                            |
+------------------------------------------------------------------+
| KPI CARD 1 | KPI CARD 2 | KPI CARD 3 | KPI CARD 4                |
+------------------------------------------------------------------+
|                                                                  |
|                  MAIN CHARTS / ANALYSIS                          |
|                                                                  |
+------------------------------------------------------------------+
|             SUPPORTING CHARTS / TABLES                            |
+------------------------------------------------------------------+
| Tooltips, drill-downs and supporting information                 |
+------------------------------------------------------------------+
```

## 3. Page 1 — Executive Overview

**Purpose:** Provide a high-level view of overall payment transaction performance.

```text
+------------------------------------------------------------------+
| EXECUTIVE OVERVIEW                                               |
+------------------------------------------------------------------+
| Date | Status | Transaction Type | Payment Method | Channel       |
+------------------------------------------------------------------+
| Total       | Transaction | Average       | Successful           |
| Transactions| Value       | Amount        | Transactions        |
+------------------------------------------------------------------+
| Failed      | Success     | Failure       | Total Refund /       |
| Transactions| Rate        | Rate          | Chargeback Summary   |
+------------------------------------------------------------------+
| Transaction Volume Trend       | Transaction Value Trend         |
|                                |                                  |
+------------------------------------------------------------------+
| Success vs Failure Comparison  | Transaction Status Distribution |
|                                |                                  |
+------------------------------------------------------------------+
| Business Summary / Key Findings                                  |
+------------------------------------------------------------------+
```

**Planned visuals**
- KPI cards for the nine required executive KPIs.
- Line charts for transaction volume and value trends.
- Comparison chart for successful versus failed transactions.
- Status distribution chart.
- Short business summary.

## 4. Page 2 — Transactions & Payment Methods

**Purpose:** Analyze transaction performance and payment method behavior.

```text
+------------------------------------------------------------------+
| TRANSACTIONS & PAYMENT METHODS                                   |
+------------------------------------------------------------------+
| Date | Status | Type | Payment Method | Provider | Channel        |
+------------------------------------------------------------------+
| Total Transactions | Transaction Value | Average Transaction Amt  |
+------------------------------------------------------------------+
| Transaction Volume / Value Trend                                 |
|                                                                  |
+------------------------------------------------------------------+
| Transaction Volume by Method | Transaction Value by Method       |
+------------------------------------------------------------------+
| Success / Failure by Method  | Provider Comparison               |
+------------------------------------------------------------------+
| Transaction Type Comparison | Channel Comparison                 |
+------------------------------------------------------------------+
```

**Planned visuals**
- Transaction volume and value trend.
- Payment method volume and value comparisons.
- Success/failure by payment method.
- Provider, transaction type and channel comparisons.

## 5. Page 3 — Customer & Merchant

**Purpose:** Analyze customer activity and merchant performance.

```text
+------------------------------------------------------------------+
| CUSTOMER & MERCHANT                                              |
+------------------------------------------------------------------+
| Date | Customer Type | Merchant Category | Merchant Type | State  |
+------------------------------------------------------------------+
| Customer Transaction Count | Customer Value | Avg Customer Amount |
+------------------------------------------------------------------+
| Merchant Transaction Count | Merchant Value | Avg Merchant Amount |
+------------------------------------------------------------------+
| Top Customers by Value       | Top Customers by Transaction Count |
+------------------------------------------------------------------+
| Top Merchants by Value       | Top Merchants by Transaction Count |
+------------------------------------------------------------------+
| Customer Type Comparison     | Merchant Category Comparison       |
+------------------------------------------------------------------+
| Customer Location Analysis   | Merchant Location Analysis        |
+------------------------------------------------------------------+
```

**Planned visuals**
- Top customers by transaction value and count.
- Top merchants by transaction value and count.
- Customer type and merchant category comparisons.
- Customer and merchant location analysis.
- Ranking tables with appropriate supporting details.

## 6. Page 4 — Location & Trends

**Purpose:** Analyze geographic and time-based transaction patterns.

```text
+------------------------------------------------------------------+
| LOCATION & TRENDS                                                |
+------------------------------------------------------------------+
| Date | City | State | Status | Transaction Type | Channel          |
+------------------------------------------------------------------+
| Total Transactions | Transaction Value | Success Rate | Failure Rate|
+------------------------------------------------------------------+
| Daily / Weekly / Monthly Transaction Volume Trend                |
+------------------------------------------------------------------+
| Transaction Value Trend       | Success / Failure Trend          |
+------------------------------------------------------------------+
| City Transaction Volume       | State Transaction Volume         |
+------------------------------------------------------------------+
| Transaction Value by Location | Geographic Map (if suitable)     |
+------------------------------------------------------------------+
```

**Planned visuals**
- Daily, weekly and monthly line charts.
- Transaction value and success/failure trends.
- City and state comparison bar charts.
- Map visual where geographic fields and mapping support are suitable.

## 7. Navigation Requirements

- Provide navigation between all four dashboard pages.
- Use consistent page titles and navigation placement.
- Make the selected page clear to the user.
- Allow users to return to Executive Overview easily.
- Validate slicer interactions and cross-filtering during implementation.

## 8. Interaction Requirements

- **Slicers:** Filter relevant charts and KPIs.
- **Tooltips:** Display supporting values and details.
- **Drill-down:** Support time or geographic drill-down where fields allow.
- **Cross-filtering:** Allow chart selections to filter related visuals where appropriate.
- **Tables:** Support detailed customer and merchant ranking analysis.

## 9. Design Recommendations

- Keep the most important KPIs near the top.
- Maintain a consistent layout across all four pages.
- Use line charts for trends and bar charts for category comparisons.
- Avoid overcrowding pages with too many visuals.
- Confirm global versus page-specific slicers before implementation.
- Decide final colors and themes after reviewing the requirements.

## 10. Assumptions and Limitations

- Layouts are preliminary and subject to stakeholder review.
- KPI calculations must follow the rules documented in `docs/kpi_definitions.md`.
- Currency, transaction status, refund status and chargeback status rules require confirmation.
- Location visuals depend on available data and mapping suitability.
- The final production Power BI dashboard is outside the scope of Day 1.
