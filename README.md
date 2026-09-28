# Payment Transaction Analytics System

## 1. Project Overview

The Payment Transaction Analytics System is an end-to-end data analytics project designed to analyze payment transactions, customer behavior, merchant performance, payment methods, refunds, and chargebacks.

The project uses manually maintained CSV files as source data. Python is used for data ingestion and validation, PostgreSQL is used for data storage, SQL is used for data transformation and analysis, and Power BI is used for reporting and visualization.

---

## 2. Business Problem

Payment platforms generate a large volume of transactions across customers, merchants, payment methods, channels, and locations.

The business needs to understand:

- Transaction volume and transaction value
- Successful and failed transactions
- Payment method performance
- Merchant performance
- Customer transaction behavior
- Transaction failure reasons
- Refund trends
- Chargeback trends
- Transaction trends over time

The goal is to build a centralized analytics solution that converts raw payment data into reliable business insights.

---

## 3. Project Objectives

- Build an end-to-end payment analytics pipeline.
- Ingest payment data from CSV files.
- Validate and clean source data.
- Store data in PostgreSQL.
- Transform raw data into analytics-ready datasets.
- Create business KPIs.
- Build Power BI dashboards.
- Implement data-quality testing.
- Maintain the project using Git and GitHub.
- Follow a structured team development workflow.

---

## 4. Source Data

The project uses manually maintained CSV files.

```text
data/
├── raw/
│   ├── customers.csv
│   ├── merchants.csv
│   ├── payment_methods.csv
│   ├── transactions.csv
│   ├── refunds.csv
│   └── chargebacks.csv
│
├── sample/
└── processed/


## 6. Technology Stack

### Programming & Data Processing
- Python
- Pandas
- NumPy
- seaborn 

### Database
- PostgreSQL
- SQL

### Data Transformation
- dbt
- SQL

### Data Quality & Testing
- Pytest
- dbt Tests

### Data Visualization
- Power BI
- DAX

### Version Control & Collaboration
- Git
- GitHub
- Jira

### CI/CD
- GitHub Actions

### Development Environment
- Visual Studio Code

---

## 7. Project Structure

```text
payment-transaction-analytics/
│
├── data/
│   ├── raw/
│   │   ├── customers.csv
│   │   ├── merchants.csv
│   │   ├── payment_methods.csv
│   │   ├── transactions.csv
│   │   ├── refunds.csv
│   │   └── chargebacks.csv
│   │
│   ├── sample/
│   └── processed/
│
├── src/
│   ├── ingestion/
│   ├── validation/
│   ├── transformation/
│   ├── database/
│   └── utils/
│
├── sql/
│   ├── ddl/
│   ├── staging/
│   ├── transformations/
│   └── marts/
│
├── tests/
│   ├── unit/
│   └── integration/
│
├── notebooks/
│
├── powerbi/
│
├── config/
│
├── docs/
│   ├── business_requirements.md
│   ├── data_dictionary.md
│   ├── project_architecture.md
│   ├── kpi_definitions.md
│   └── team_tasks.md
│
├── .github/
│   └── workflows/
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md