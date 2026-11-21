import pandas as pd

# Load the dataset from data/raw
df = pd.read_excel("data/raw/Online Retail.xlsx")

# Check basic info
print("Rows & Columns:", df.shape)
print("\nColumns:", df.columns.tolist())
print("\nFirst 5 rows:")
print(df.head())