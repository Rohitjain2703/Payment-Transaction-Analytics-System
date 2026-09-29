
# Payment Transaction Analytics  System

An end-to-end payment analytics, data science, and machine learning project for analyzing payment transactions, identifying fraud and transaction-risk patterns, generating business KPIs, and providing data-driven insights through Power BI.

---

## 1. Project Overview

The Payment Transaction Analytics & Fraud Detection System is an end-to-end data analytics and machine learning platform built using Python, PostgreSQL, SQL, Machine Learning, and Power BI.

The project processes payment transaction data from CSV files, loads the data into PostgreSQL, performs data validation and transformation, conducts exploratory data analysis, creates machine learning features, trains fraud detection models, evaluates model performance, and presents business insights through Power BI dashboards.

The project is designed as a collaborative team project following Git, GitHub, feature branches, pull requests, code reviews, and modular development practices.

---

## 2. Business Objectives

The main objectives of the project are:

- Analyze payment transaction behavior
- Monitor transaction success and failure
- Identify suspicious transaction patterns
- Analyze refunds and chargebacks
- Identify customer and merchant risk patterns
- Build fraud-related machine learning features
- Develop fraud detection models
- Evaluate machine learning model performance
- Generate business KPIs
- Build interactive Power BI dashboards
- Create a reusable and scalable data science pipeline

---

## 3. End-to-End Architecture

```text
                    CSV DATA
                       |
                       v
              Python Data Ingestion
                       |
                       v
               Data Validation
                       |
                       v
                  PostgreSQL
                       |
          +------------+------------+
          |                         |
          v                         v
    SQL Transformations       Data Analysis
          |                         |
          v                         v
   Analytics Tables              EDA
          |                         |
          +------------+------------+
                       |
                       v
              Feature Engineering
                       |
                       v
                 ML Dataset
                       |
                       v
              Fraud Detection ML
                       |
          +------------+------------+
          |            |            |
          v            v            v
      Baseline      XGBoost      LightGBM
       Model
          |            |            |
          +------------+------------+
                       |
                       v
               Model Evaluation
                       |
                       v
                 Best Model
                       |
                       v
                  Joblib Model
                       |
                       v
                  FastAPI
                       |
                       v
               Fraud Prediction
                       |
                       v
                  Power BI
                       |
                       v
              Business Insights

Source Datasets

The project uses six payment-related CSV datasets.

customers.csv

Customer master information.

Columns:

customer_id
customer_name
email
phone
city
state
customer_type
registration_date
merchants.csv

Merchant master information.

Columns:

merchant_id
merchant_name
category
city
state
merchant_type
registration_date
payment_methods.csv

Customer payment method information.

Columns:

payment_method_id
customer_id
method_type
provider
last_four_digits
is_default
created_date
transactions.csv

Main payment transaction dataset.

Columns:

transaction_id
customer_id
merchant_id
payment_method_id
transaction_date
amount
currency
transaction_status
transaction_type
channel
city
state
refunds.csv

Refund transaction information.

Columns:

refund_id
transaction_id
customer_id
merchant_id
refund_date
refund_amount
refund_reason
refund_status
chargebacks.csv

Chargeback information.

Columns:

chargeback_id
transaction_id
customer_id
merchant_id
chargeback_date
chargeback_amount
chargeback_reason
chargeback_status
5. Data Relationships
customers
    |
    | customer_id
    v
transactions
    |
    +----------------------+
    |                      |
    v                      v
merchants          payment_methods
    |
    |
    +----------------------+
                           |
                    transaction_id
                           |
                 +---------+---------+
                 |                   |
                 v                   v
              refunds           chargebacks
6. Data Engineering Workflow

The data engineering pipeline follows:

CSV Files
    |
    v
Python Ingestion
    |
    v
Data Validation
    |
    v
PostgreSQL
    |
    v
Staging Tables
    |
    v
SQL Transformations
    |
    v
Analytics Tables
    |
    v
ML Dataset
7. Data Science Workflow

The Data Science workflow follows:

Raw Data
   |
   v
Data Cleaning
   |
   v
EDA
   |
   v
Business Understanding
   |
   v
Feature Engineering
   |
   v
Feature Selection
   |
   v
ML Dataset
   |
   v
Train / Validation / Test
   |
   v
Baseline Model
   |
   v
Model Training
   |
   v
Hyperparameter Tuning
   |
   v
Model Evaluation
   |
   v
Model Selection
   |
   v
Prediction
8. Machine Learning Objective

The primary machine learning objective is to identify suspicious or high-risk payment transactions using transaction, customer, merchant, refund, and chargeback information.

The project will investigate transaction risk patterns using historical transaction behavior and available chargeback/dispute information.

The target definition will be finalized by the Data Science team after analyzing the business meaning of the available chargeback and transaction data.

Important:

A chargeback should not automatically be treated as fraud. The Data Science team must define the target variable based on the available business labels and chargeback reasons.

9. Machine Learning Features

Potential features include:

Transaction Features
Transaction amount
Transaction channel
Transaction type
Transaction status
Transaction frequency
Transaction velocity
Transaction amount deviation
Customer Features
Customer transaction count
Customer average transaction amount
Customer transaction frequency
Customer failed transaction count
Customer refund rate
Customer chargeback rate
Customer historical transaction behavior
Merchant Features
Merchant transaction count
Merchant average transaction amount
Merchant success rate
Merchant failure rate
Merchant refund rate
Merchant chargeback rate
Payment Features
Payment method type
Payment provider
Payment method usage frequency
Payment method transaction amount
Time-Based Features
Transaction hour
Transaction day
Transaction day of week
Transaction month
Weekend indicator
High-frequency transaction indicator
10. Machine Learning Models

The project will compare multiple machine learning algorithms.

Baseline Model
Logistic Regression
Tree-Based Models
Decision Tree
Random Forest
Gradient Boosting Models
XGBoost
LightGBM

The final model will be selected based on business requirements and evaluation metrics rather than accuracy alone.

11. Model Evaluation

The following metrics will be evaluated:

Precision
Recall
F1 Score
ROC-AUC
PR-AUC
Confusion Matrix

For fraud detection, special attention will be given to:

Precision
Recall
F1 Score
PR-AUC

Accuracy alone will not be used as the primary model selection metric because fraud/risk datasets can be highly imbalanced.

12. Exploratory Data Analysis

EDA will cover:

Transaction Analysis
Transaction volume
Transaction amount distribution
Success/failure trends
Daily transaction trends
Monthly transaction trends
Channel analysis
Customer Analysis
Customer transaction behavior
High-value customers
Customer transaction frequency
Customer failure patterns
Merchant Analysis
Merchant transaction volume
Merchant transaction value
Merchant success rate
Merchant failure rate
Merchant risk patterns
Refund Analysis
Refund volume
Refund amount
Refund reasons
Refund trends
Chargeback Analysis
Chargeback volume
Chargeback amount
Chargeback reasons
Chargeback trends
13. Business KPIs

The project will calculate:

Total Transactions
Total Transaction Value
Successful Transactions
Failed Transactions
Transaction Success Rate
Transaction Failure Rate
Average Transaction Value
Total Customers
Total Merchants
Total Refund Amount
Refund Rate
Total Chargeback Amount
Chargeback Rate
High-Risk Transaction Count
Fraud/Risk Rate
Model Precision
Model Recall
Model F1 Score
Model ROC-AUC
Model PR-AUC
14. Technology Stack
Programming
Python
SQL
Data Processing
Pandas
NumPy
SciPy
Data Visualization
Matplotlib
Seaborn
Database
PostgreSQL
Machine Learning
Scikit-learn
XGBoost
LightGBM
Model Explainability
SHAP
Model Serialization
Joblib
API
FastAPI
Uvicorn
Testing
Pytest
Pytest-Cov
BI / Reporting
Power BI
Development Tools
Visual Studio Code
Git
GitHub
GitHub Actions
15. Project Structure
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
│   │   ├── extract_transactions.py
│   │   ├── load_transactions.py
│   │   └── __init__.py
│   │
│   ├── validation/
│   │   ├── data_quality.py
│   │   └── __init__.py
│   │
│   ├── transformation/
│   │   ├── clean_transactions.py
│   │   ├── feature_engineering.py
│   │   └── __init__.py
│   │
│   ├── database/
│   │   ├── connection.py
│   │   ├── postgres_loader.py
│   │   └── __init__.py
│   │
│   ├── data_processing/
│   │
│   ├── feature_engineering/
│   │
│   ├── ml/
│   │   ├── training/
│   │   ├── evaluation/
│   │   ├── prediction/
│   │   └── utils/
│   │
│   └── utils/
│       ├── config_loader.py
│       ├── logger.py
│       └── __init__.py
│
├── sql/
│   ├── ddl/
│   ├── staging/
│   ├── transformations/
│   └── marts/
│
├── notebooks/
│   ├── eda/
│   ├── feature_engineering/
│   └── modeling/
│
├── models/
│
├── experiments/
│
├── api/
│
├── tests/
│   ├── unit/
│   ├── integration/
│   └── ml/
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
│   ├── team_tasks.md
│   └── ml/
│
├── .github/
│   └── workflows/
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
16. Folder Responsibilities
data/raw

Contains the original project CSV datasets.

data/processed

Contains cleaned or transformed datasets generated during processing.

src/ingestion

Responsible for reading and loading source data.

src/validation

Responsible for data quality checks.

src/transformation

Responsible for data cleaning and transformations.

src/database

Responsible for PostgreSQL connectivity and loading.

src/feature_engineering

Responsible for creating reusable ML features.

src/ml/training

Contains model training code.

src/ml/evaluation

Contains model evaluation code.

src/ml/prediction

Contains prediction/inference code.

notebooks/eda

Contains exploratory data analysis notebooks.

notebooks/feature_engineering

Contains feature engineering experiments.

notebooks/modeling

Contains machine learning experiments.

models

Stores trained model artifacts when required.

api

Contains FastAPI application code for model prediction.

powerbi

Contains Power BI project/dashboard documentation and related assets.

tests

Contains unit, integration, data-quality, and ML tests.

17. PostgreSQL Architecture

PostgreSQL will be the primary database for the project.

The database architecture will follow:

PostgreSQL
│
├── raw
│
├── staging
│
└── analytics
Raw Layer

Stores data loaded from CSV files.

Staging Layer

Contains cleaned and standardized data.

Analytics Layer

Contains business-ready analytical tables and ML-ready datasets.

18. SQL Responsibilities

SQL will be used for:

Data cleaning
Data transformation
Table joins
Aggregations
KPI calculations
Customer analytics
Merchant analytics
Transaction analytics
Refund analysis
Chargeback analysis
Feature preparation
ML dataset preparation
19. Power BI Dashboard

The Power BI dashboard will contain multiple sections.

Executive Dashboard
Total Transactions
Transaction Value
Success Rate
Failure Rate
Refund Rate
Chargeback Rate
Risk/Fraud Rate
Transaction Dashboard
Daily transactions
Monthly transactions
Transaction amount trends
Channel analysis
Transaction status
Customer Dashboard
Customer transaction behavior
Top customers
Customer transaction value
Customer risk patterns
Merchant Dashboard
Merchant performance
Merchant transaction volume
Merchant success rate
Merchant risk patterns
Fraud / Risk Dashboard
High-risk transactions
Risk trends
Chargeback trends
Risk by merchant
Risk by customer
Risk by channel
Model performance
20. Team Structure

The project follows a cross-functional team structure.

Team Lead

Responsibilities:

Project architecture
Requirement definition
Dataset management
Task allocation
GitHub management
Branch management
Code review
Pull request review
Integration
Final testing
Team coordination
Data Engineer

Responsibilities:

CSV ingestion
PostgreSQL database
Data loading
Data pipelines
Data validation
Database optimization
Data Analysts

Responsibilities:

SQL analysis
KPI development
Business analysis
Transaction analysis
Customer analysis
Merchant analysis
Refund analysis
Chargeback analysis
Data Scientist - EDA

Responsibilities:

Exploratory Data Analysis
Statistical analysis
Fraud/risk pattern analysis
Feature analysis
Business insights
Data Scientist - Feature Engineering

Responsibilities:

Customer features
Merchant features
Transaction features
Time-based features
Risk features
Feature selection
ML Engineer / Data Scientist - Modeling

Responsibilities:

Baseline model
Random Forest
XGBoost
LightGBM
Hyperparameter tuning
Model evaluation
Model comparison
ML Engineer - Production

Responsibilities:

Model serialization
Prediction pipeline
FastAPI
API testing
Model integration
Dockerization if required
Power BI Developers

Responsibilities:

Data model
DAX measures
Dashboard development
KPI visualization
Fraud/risk dashboard
21. Git Workflow

The project follows a feature-branch workflow.

main
  ↑
develop
  ↑
feature branches

Example branches:

feature/csv-ingestion
feature/postgresql-schema
feature/data-validation
feature/sql-analytics
feature/eda
feature/feature-engineering
feature/fraud-model
feature/model-evaluation
feature/prediction-api
feature/powerbi-dashboard

Developers should not directly push development code to main.

Expected workflow:

Create Feature Branch
        ↓
Development
        ↓
Local Testing
        ↓
Commit
        ↓
Push Branch
        ↓
Pull Request
        ↓
Code Review
        ↓
Merge into develop
        ↓
Integration Testing
        ↓
Merge into main
22. Development Standards

All team members should:

Follow the project folder structure
Use meaningful variable and function names
Write modular code
Add tests for important functionality
Avoid hardcoded credentials
Use .env for local configuration
Keep commits focused
Create feature branches
Raise Pull Requests
Request code review before merging
Update documentation when required
23. Testing Strategy

Testing will cover:

Data Tests
Null checks
Duplicate checks
Data type validation
Referential integrity
Invalid values
Unit Tests
Python functions
Data transformations
Feature engineering
ML Tests
Feature schema validation
Prediction output validation
Model input validation
Model output validation
Integration Tests
CSV to PostgreSQL
PostgreSQL to ML pipeline
API prediction flow
24. Project Development Phases
Phase 1 - Project Setup
Repository setup
Folder structure
Git workflow
Team allocation
Dataset setup
Phase 2 - Data Engineering
CSV ingestion
Data validation
PostgreSQL schema
Data loading
Phase 3 - Data Analysis
SQL analysis
EDA
Business KPIs
Transaction analysis
Phase 4 - Feature Engineering
Customer features
Merchant features
Transaction features
Risk features
ML dataset
Phase 5 - Machine Learning
Target definition
Train/test split
Baseline model
Random Forest
XGBoost
LightGBM
Hyperparameter tuning
Phase 6 - Model Evaluation
Precision
Recall
F1
ROC-AUC
PR-AUC
Confusion Matrix
Model comparison
Phase 7 - ML API
Model serialization
FastAPI
Prediction endpoint
API testing
Phase 8 - Business Intelligence
Power BI data model
DAX measures
Dashboards
Risk dashboard
Phase 9 - Integration
End-to-end testing
Code review
Documentation
Final validation
25. Current Project Status
Completed
Project repository created
GitHub repository configured
Project folder structure created
Six CSV datasets added
Data dictionary created
README created
Data Engineering structure created
Data Science / ML structure created
Python requirements defined
In Progress
Virtual environment setup
PostgreSQL setup
Data validation
PostgreSQL schema
EDA
Feature engineering
ML target definition
Planned
Fraud detection model
Model evaluation
Prediction API
Power BI risk dashboard
End-to-end integration
Automated testing
Final documentation
26. Important Project Principle

The project is designed as an end-to-end production-style Data Science and Analytics system.

The goal is not only to build a machine learning model.

The complete solution should demonstrate:

Data Engineering
       +
SQL
       +
Data Analysis
       +
Statistics
       +
Feature Engineering
       +
Machine Learning
       +
Model Evaluation
       +
API
       +
Business Intelligence
       +
Testing
       +
Git/GitHub