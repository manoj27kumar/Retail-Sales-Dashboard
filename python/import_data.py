import pandas as pd
from sqlalchemy import create_engine

# Read CSV
df = pd.read_csv(r"D:\portfolio projects\retail-sales-dashboard\data\Sample- Superstore.csv")

# Convert dates
df["Order Date"] = pd.to_datetime(df["Order Date"], format="mixed")
df["Ship Date"] = pd.to_datetime(df["Ship Date"], format="mixed")

# Rename columns to match MySQL table
df.columns = [
    "row_id",
    "order_id",
    "order_date",
    "ship_date",
    "ship_mode",
    "customer_id",
    "segment",
    "country",
    "city",
    "state",
    "region",
    "product_id",
    "category",
    "sub_category",
    "product_name",
    "sales",
    "quantity",
    "discount",
    "profit"
]

# Connect to MySQL
engine = create_engine(
    "mysql+pymysql://root:root@localhost/retail_sales"
    
)

# Import into MySQL
df.to_sql(
    "orders",
    engine,
    if_exists="append",
    index=False
)

print(f"Imported {len(df)} rows successfully!")