

CREATE TABLE transactions (
    transaction_id VARCHAR(50),
    customer_id VARCHAR(50),
    merchant_id VARCHAR(50),
    payment_method_id VARCHAR(50),
    transaction_date TIMESTAMP,
    amount NUMERIC(12, 2),
    currency VARCHAR(10),
    transaction_status VARCHAR(30),
    transaction_type VARCHAR(50),
    channel VARCHAR(50),
    city VARCHAR(100),
    state VARCHAR(100)
);

CREATE TABLE payment_methods (
    payment_method_id VARCHAR(50),
    customer_id VARCHAR(50),
    method_type VARCHAR(50),
    provider VARCHAR(100),
    last_four_digits VARCHAR(10),
    is_default VARCHAR(10),
    created_date TIMESTAMP
);

select * from payment_methods;


CREATE TABLE transactions_staging (
    transaction_id TEXT,
    customer_id TEXT,
    merchant_id TEXT,
    payment_method_id TEXT,
    transaction_date TEXT,
    amount TEXT,
    currency TEXT,
    transaction_status TEXT,
    transaction_type TEXT,
    channel TEXT,
    city TEXT,
    state TEXT
);



SELECT COUNT(*) AS total_rows
FROM public.transactions_staging;

SELECT
    COUNT(*) AS total_rows,
    COUNT(NULLIF(TRIM(amount), '')) AS amount_filled,
    COUNT(*) FILTER (
        WHERE UPPER(TRIM(amount)) = 'N/A'
    ) AS amount_na,
    COUNT(*) FILTER (
        WHERE TRIM(amount) = ''
    ) AS amount_blank
FROM public.transactions_staging;



DROP TABLE IF EXISTS public.transactions_clean;

CREATE TABLE public.transactions_clean AS
SELECT
    NULLIF(TRIM(transaction_id), '') AS transaction_id,
    NULLIF(TRIM(customer_id), '') AS customer_id,
    NULLIF(TRIM(merchant_id), '') AS merchant_id,
    NULLIF(TRIM(payment_method_id), '') AS payment_method_id,

    CASE
        WHEN TRIM(transaction_date) = ''
          OR UPPER(TRIM(transaction_date)) = 'N/A'
        THEN NULL
        ELSE TRIM(transaction_date)::timestamp
    END AS transaction_date,

    CASE
        WHEN TRIM(amount) = ''
          OR UPPER(TRIM(amount)) = 'N/A'
        THEN NULL
        ELSE TRIM(amount)::numeric(12,2)
    END AS amount,

    NULLIF(TRIM(currency), '') AS currency,
    NULLIF(LOWER(TRIM(transaction_status)), '') AS transaction_status,
    NULLIF(TRIM(transaction_type), '') AS transaction_type,
    NULLIF(TRIM(channel), '') AS channel,
    NULLIF(TRIM(city), '') AS city,
    NULLIF(TRIM(state), '') AS state
FROM public.transactions_staging;



SELECT
    COUNT(*) AS total_rows,
    COUNT(amount) AS valid_amounts,
    COUNT(*) - COUNT(amount) AS missing_amounts
FROM public.transactions_clean;


SELECT
    COUNT(*) AS total_rows,
    COUNT(payment_method_id) AS available_ids,
    COUNT(*) - COUNT(payment_method_id) AS missing_ids,
    COUNT(DISTINCT payment_method_id) AS unique_ids
FROM public.payment_methods;


DROP TABLE IF EXISTS public.payment_methods_clean;

CREATE TABLE public.payment_methods_clean AS
SELECT DISTINCT ON (payment_method_id)
    payment_method_id,
    customer_id,
    method_type,
    provider,
    last_four_digits,
    is_default,
    created_date
FROM public.payment_methods
WHERE payment_method_id IS NOT NULL
  AND TRIM(payment_method_id) <> ''
ORDER BY payment_method_id;


SELECT
    COUNT(*) AS total_rows,
    COUNT(DISTINCT payment_method_id) AS unique_ids,
    COUNT(*) - COUNT(payment_method_id) AS missing_ids
FROM public.payment_methods_clean;


select * from payment_methods_clean;


-- Total Payment Methods
select count(*) as total_payment_methods	
from payment_methods_clean

-- Payment Method Types
select
	method_type,
	count(*) as payment_method_count
from payment_methods_clean
group by method_type
order by payment_method_count desc;

--Payment Method Providers
select
	provider,
	count(*) as payment_method_count
from payment_methods_clean
group by provider
order by payment_method_count desc; 

--Number of Customers Using Each Payment Method
select
	method_type,
	count(distinct customer_id) as unique_customers
from payment_methods_clean
where method_type is not null
and customer_id is not null
group by method_type
order by unique_customers desc; 

--Default Payment Method Information
select
is_default,
count(*) as payment_method_count
from payment_methods_clean
group by is_default
order by payment_method_count desc;

--there is showing multiple values then we use case to resolve this issue
select 
	case
		when lower(trim(is_default::text)) in ('true','Yes','1','TRUE')
		then 'True'
		when lower(trim(is_default::text)) in ('false','o','FALSE','No')
		then 'False'
	end as default_status,
	count(*) as payment_method_count
from payment_methods_clean
group by default_status
order by payment_method_count desc;

--Missing Values
select * from payment_methods_clean

select
	count(*) filter (where payment_method_id is null) as missing_payment_id,
	count(*) filter (where customer_id is null) as missing_customer_id,
	count(*) filter (where Method_type is null) as missing_method_type,
	count(*) filter (where provider is null) as missing_provider,
	count(*) filter (where last_four_digits is null) as missing_last_four_digits,
	count(*) filter (where is_default is null) as missing_is_default,
	count(*) filter (where created_date is null) as missing_created_date
from payment_methods_clean


--Duplicate Payment Method Records
select
	payment_method_id,
	count(*) as record_count
from payment_methods_clean
group by payment_method_id
having count(*)>1
order by record_count desc

--Payment Method Usage

select * from payment_methods_clean
select * from transactions_clean

--Transaction Count by Payment Method
select
	pm.method_type,
	count(*) as transaction_count
from transactions_clean t
left join payment_methods_clean pm
on t.customer_id = pm.customer_id
group by pm.method_type
order by transaction_count desc;