# Payment Transaction Analytics System - Data Dictionary

## 1. customers.csv

| Column | Description | Type | Key |
|---|---|---|---|
| customer_id | Unique customer identifier | VARCHAR | Primary Key |
| customer_name | Customer full name | VARCHAR | |
| email | Customer email address | VARCHAR | |
| phone | Customer phone number | VARCHAR | |
| city | Customer city | VARCHAR | |
| state | Customer state | VARCHAR | |
| customer_type | Customer classification | VARCHAR | |
| registration_date | Customer registration date | DATE | |

---

## 2. merchants.csv

| Column | Description | Type | Key |
|---|---|---|---|
| merchant_id | Unique merchant identifier | VARCHAR | Primary Key |
| merchant_name | Merchant name | VARCHAR | |
| category | Merchant business category | VARCHAR | |
| city | Merchant city | VARCHAR | |
| state | Merchant state | VARCHAR | |
| merchant_type | Merchant classification | VARCHAR | |
| registration_date | Merchant registration date | DATE | |

---

## 3. payment_methods.csv

| Column | Description | Type | Key |
|---|---|---|---|
| payment_method_id | Unique payment method identifier | VARCHAR | Primary Key |
| customer_id | Customer associated with payment method | VARCHAR | Foreign Key |
| method_type | Type of payment method | VARCHAR | |
| provider | Payment provider | VARCHAR | |
| last_four_digits | Last four digits of payment instrument | VARCHAR | |
| is_default | Indicates default payment method | BOOLEAN | |
| created_date | Payment method creation date | DATE | |

---

## 4. transactions.csv

| Column | Description | Type | Key |
|---|---|---|---|
| transaction_id | Unique transaction identifier | VARCHAR | Primary Key |
| customer_id | Customer who made transaction | VARCHAR | Foreign Key |
| merchant_id | Merchant receiving transaction | VARCHAR | Foreign Key |
| payment_method_id | Payment method used | VARCHAR | Foreign Key |
| transaction_date | Date/time of transaction | TIMESTAMP | |
| amount | Transaction amount | DECIMAL | |
| currency | Transaction currency | VARCHAR | |
| transaction_status | Transaction processing status | VARCHAR | |
| transaction_type | Type of transaction | VARCHAR | |
| channel | Transaction channel | VARCHAR | |
| city | Transaction city | VARCHAR | |
| state | Transaction state | VARCHAR | |

---

## 5. refunds.csv

| Column | Description | Type | Key |
|---|---|---|---|
| refund_id | Unique refund identifier | VARCHAR | Primary Key |
| transaction_id | Original transaction identifier | VARCHAR | Foreign Key |
| customer_id | Customer receiving refund | VARCHAR | Foreign Key |
| merchant_id | Merchant associated with refund | VARCHAR | Foreign Key |
| refund_date | Date of refund | DATE/TIMESTAMP | |
| refund_amount | Refunded amount | DECIMAL | |
| refund_reason | Reason for refund | VARCHAR | |
| refund_status | Refund processing status | VARCHAR | |

---

## 6. chargebacks.csv

| Column | Description | Type | Key |
|---|---|---|---|
| chargeback_id | Unique chargeback identifier | VARCHAR | Primary Key |
| transaction_id | Original transaction identifier | VARCHAR | Foreign Key |
| customer_id | Customer associated with chargeback | VARCHAR | Foreign Key |
| merchant_id | Merchant associated with chargeback | VARCHAR | Foreign Key |
| chargeback_date | Date of chargeback | DATE/TIMESTAMP | |
| chargeback_amount | Chargeback amount | DECIMAL | |
| chargeback_reason | Reason for chargeback | VARCHAR | |
| chargeback_status | Chargeback processing status | VARCHAR | |

---

# Dataset Relationships

## Customer Relationship

customers.customer_id
↓
transactions.customer_id

## Merchant Relationship

merchants.merchant_id
↓
transactions.merchant_id

## Payment Method Relationship

payment_methods.payment_method_id
↓
transactions.payment_method_id

## Refund Relationship

transactions.transaction_id
↓
refunds.transaction_id

## Chargeback Relationship

transactions.transaction_id
↓
chargebacks.transaction_id