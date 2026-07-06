from sqlalchemy import create_engine

# Change the password if yours is different
engine = create_engine(
    "mysql+pymysql://root:root@localhost/retail_sales"
)