import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
dbname = os.getenv("DB_NAME")

engine = create_engine(f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}")

df = pd.read_csv("data/processed/cleaned_online_retail.csv")
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

df.to_sql("sales_transactions", engine, if_exists="replace", index=False, chunksize=10000)
print("Success! Loaded", len(df), "rows into 'sales_transactions' table.")