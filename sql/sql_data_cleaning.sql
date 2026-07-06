
create database retail_sales;
use retail_sales;
select database();
show tables;
CREATE TABLE orders (
    row_id INT PRIMARY KEY,
    order_id VARCHAR(20),
    order_date DATE,
    ship_date DATE,
    ship_mode VARCHAR(30),
    customer_id VARCHAR(20),
    segment VARCHAR(30),
    country VARCHAR(50),
    city VARCHAR(50),
    state VARCHAR(50),
    region VARCHAR(20),
    product_id VARCHAR(30),
    category VARCHAR(30),
    sub_category VARCHAR(30),
    product_name VARCHAR(255),
    sales DECIMAL(10,4),
    quantity INT,
    discount DECIMAL(4,2),
    profit DECIMAL(10,4)
);

describe orders;

select count(*) as total_orders
from orders;
show tables;

SELECT COUNT(*) FROM orders;

SELECT * FROM orders LIMIT 5;

SHOW GLOBAL VARIABLES LIKE 'local_infile';

LOAD DATA LOCAL INFILE  'D:/portfolio projects/retail-sales-dashboard/data/Sample-Superstore.csv'
INTO TABLE orders
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(
row_id,
order_id,
@order_date,
@ship_date,
ship_mode,
customer_id,
segment,
country,
city,
state,
region,
product_id,
category,
sub_category,
product_name,
sales,
quantity,
discount,
profit
)
SET
order_date = STR_TO_DATE(@order_date, '%d-%m-%Y'),
ship_date = STR_TO_DATE(@ship_date, '%d-%m-%Y');

use retail_sales;

select count(*) from orders;


