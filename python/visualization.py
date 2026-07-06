import pandas as pd
import matplotlib.pyplot as plt
from db_connection import engine

# Load data
query = "SELECT * FROM orders"
df = pd.read_sql(query, engine)

print(df.head())
print(df.info())

# Chart 1 - Sales by region 

region_sales = (
    df.groupby("region")["sales"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(8,5))
region_sales.plot(kind="bar")

plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")

plt.tight_layout()
plt.savefig("images/sales_by_region.png")
plt.show()

# Chart - 2 Profit by category

category_profit = (
    df.groupby("category")["profit"]
    .sum()
)

plt.figure(figsize=(8,5))
category_profit.plot(kind="bar")

plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Profit")

plt.tight_layout()
plt.savefig("images/profit_by_category.png")
plt.show()

# Monthly Sales Trend

df["order_date"] = pd.to_datetime(df["order_date"])

monthly_sales = (
    df.groupby(df["order_date"].dt.to_period("M"))["sales"]
    .sum()
)

plt.figure(figsize=(12,5))
monthly_sales.plot()

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("sales")

plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("images/monthly_sales.png")
plt.show()

# Chart - 4 Sales by Segment

sales_segment = (
    df.groupby("segment")["sales"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(8,5))
sales_segment.plot(kind="pie",autopct="%1.1f%%")

plt.ylabel=""
plt.title("Sales by Segment")

plt.tight_layout()
plt.savefig("images/sales_by_segment.png")
plt.show()

# Chart - 5 Top 10 products

top_products = (
    df.groupby("product_name")["sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(12,8))
top_products.sort_values().plot(kind="barh")

plt.title("Top 10 Products by Sales")
plt.xlabel("Sales")

plt.tight_layout()
plt.savefig("images/top_10_products.png")
plt.show()

