#connect to mysql
import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "mysql+pymysql://root:root@localhost/retail_sales"
)



df = pd.read_sql("SELECT * FROM orders",engine)


# Convert date columns
df["order_date"] = pd.to_datetime(df["order_date"])
df["ship_date"] = pd.to_datetime(df["ship_date"])

st.write(df.columns)
st.write(df.head())
st.write(df.shape)

# Dashboard title

st.set_page_config(
    page_title="Retail Sales Dashboard",
    layout="wide"
)

st.title("Retail Sales  Dashboard")
st.markdown("### Sales Performance Analysis")

# KPI cards
total_sales = df["sales"].sum()

total_profit = df["profit"].sum()

total_orders = len(df)

col1,col2,col3 = st.columns(3)

col1.metric(
    "Total Sales",
    f"${total_sales:,.2f}"
)

col2.metric(
    "Total Profit",
    f"${total_profit:,.2f}"
)

col3.metric(
    "Orders",
    total_orders
)

# Sidebar Filter

st.sidebar.header("Filters")

regions = st.sidebar.multiselect(
    "Select Region",
    df["region"].unique(),
    default=df["region"].unique()
)

filtered_df = df[
    df["region"].isin(regions)
]

# Monthly Sales Chart


monthly_sales = (
    filtered_df
    .groupby(
        filtered_df["order_date"].dt.to_period("M")
    )["sales"]
    .sum()
)

st.write(filtered_df.dtypes)

monthly_sales.index = monthly_sales.index.astype(str)

st.line_chart(monthly_sales)

#sales by region

region_sales = (
    filtered_df
    .groupby("region")["sales"]
    .sum()
)

st.bar_chart(region_sales)

# profit by category

category_profit = (
    filtered_df
    .groupby("category")["profit"]
    .sum()
)

st.bar_chart(category_profit)

# Top Products
top_products = (
    filtered_df
    .groupby("product_name")["sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

st.subheader("Top Products")

st.dataframe(top_products)

# Display raw data
st.subheader("Dataset")

st.dataframe(filtered_df)

# Run Dashboard