#EDA
#what is the total sales ,total profit and total orders?

select 
	round(sum(sales),2) as total_sales,
    round(sum(profit),2) as total_profit,
    count(*) as total_orders
from orders;

#Total Sales by Region
select 
	region,
	round(sum(sales),2) as total_sales
from orders
group by region
order by total_sales Desc;
#west region has generated highest sales.

#Profit by region
select
	region,
    round(sum(profit),2) as total_profit
from orders
group by region
order by total_profit Desc;
#West region has generated highest profit

#sales by category
select
	category,
    round(sum(sales),2) as total_sales
from orders
group by category
order by total_sales desc;
#Technology has generated highest sales

#Profit by category

select 
	category,
    round(sum(profit),2) as total_profit
from orders
group by category
order by total_profit desc;
# Technology has generated highest profit

# Sales by sub-category
select 
	sub_category,
    round(sum(sales),2) as total_sales
from orders
group by sub_category
order by total_sales desc;
# Phone has generated highest sales

# Top 10 Product by sales
select 
	product_name,
    round(sum(sales),2) as total_sales
from orders
group by product_name
order by total_sales desc
limit 10;

# Bottom 10 products by profit
select
	product_name,
    round(sum(profit),2) as total_profit
from orders
group by product_name
order by total_profit
limit 10;
#These products are losing money.

# Sales by customer segment 
select
	segment,
    round(sum(sales),2) as total_sales
from orders
group by segment
order by total_sales desc;

# Monthly sales Trend
select 
	date_format(order_date,'%Y-%m') as month,
    round(sum(sales),2) as total_sales
from orders
group by month
order by month ;

# Monthly profit Trend
select 
	date_format(order_date,'%Y-%m') as month,
    round(sum(profit),2) as total_profit
from orders
group by month
order by month;

# Top 10 cities by sales
select
	city,
    round(sum(sales),2) as total_sales
from orders
group by city
order by total_sales desc
limit 10;

# Average Discount by category
select
	category,
    round(avg(discount),2) as avg_discount
from orders
group by category;

# Top 10 most profitable products
select 
	product_name,
    round(sum(profit),2) as total_profit
from orders
group by product_name
order by total_profit desc
limit 10;

# Sales vs Profit by category 
select 
	category,
    round(sum(sales),2) as total_sales,
    round(sum(profit),2) as total_profit
from orders
group by category; 
    