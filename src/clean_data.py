import pandas as pd

# 1. Load raw data
df = pd.read_excel("data/raw/Online Retail.xlsx")

# 2. Remove rows with missing CustomerID or Description
df = df.dropna(subset=["CustomerID", "Description"])

# 3. Remove cancelled orders (InvoiceNo starting with 'C')
df = df[~df["InvoiceNo"].astype(str).str.startswith("C")]

# 4. Keep only positive Quantity and UnitPrice
df = df[(df["Quantity"] > 0) & (df["UnitPrice"] > 0)]

# 5. Fix data types & create TotalAmount column
df["CustomerID"] = df["CustomerID"].astype(int)
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
df["TotalAmount"] = df["Quantity"] * df["UnitPrice"]

# 6. Save cleaned dataset to data/processed
df.to_csv("data/processed/cleaned_online_retail.csv", index=False)
print("Cleaning complete! Final shape:", df.shape)