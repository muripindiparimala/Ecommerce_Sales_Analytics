"""
Chart Generation Module for EDA
Saves presentation-ready visual charts for EduSkills internship report
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configure style
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.rcParams['font.sans-serif'] = 'Arial'
plt.rcParams['axes.edgecolor'] = '#cccccc'
plt.rcParams['axes.linewidth'] = 0.8

output_dir = "notebooks/eda_charts"
os.makedirs(output_dir, exist_ok=True)

df = pd.read_csv("data/processed/cleaned_online_retail.csv")
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# 1. Monthly Revenue Trend
df['YearMonth'] = df['InvoiceDate'].dt.to_period('M').astype(str)
monthly = df.groupby('YearMonth')['TotalAmount'].sum() / 1000  # in £ thousands

fig, ax = plt.subplots(figsize=(11, 5))
monthly.plot(kind='bar', color='#1f77b4', ax=ax, width=0.7)
ax.set_title("Monthly Revenue Trend (£ Thousands) - Nov 2011 Peak Season", fontsize=14, pad=15, fontweight='bold')
ax.set_xlabel("Year-Month", fontsize=11)
ax.set_ylabel("Revenue (£K)", fontsize=11)
plt.xticks(rotation=45)
for i, v in enumerate(monthly):
    ax.text(i, v + 15, f"£{v:.0f}K", ha='center', fontsize=9, fontweight='bold')
plt.tight_layout()
fig.savefig(f"{output_dir}/01_monthly_revenue_trend.png", dpi=200)
plt.close(fig)

# 2. Top 10 Countries by Revenue (Excluding UK for visibility of global markets)
top_countries = df[df['Country'] != 'United Kingdom'].groupby('Country')['TotalAmount'].sum().sort_values(ascending=False).head(10) / 1000

fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(x=top_countries.values, y=top_countries.index, palette='viridis', ax=ax)
ax.set_title("Top 10 International Markets by Revenue (Excl. UK)", fontsize=14, pad=15, fontweight='bold')
ax.set_xlabel("Revenue (£ Thousands)", fontsize=11)
ax.set_ylabel("Country", fontsize=11)
for i, v in enumerate(top_countries.values):
    ax.text(v + 3, i, f"£{v:.1f}K", va='center', fontsize=9, fontweight='bold')
plt.tight_layout()
fig.savefig(f"{output_dir}/02_top_international_markets.png", dpi=200)
plt.close(fig)

# 3. Top 10 Best Selling Products by Revenue
top_products = df.groupby('Description')['TotalAmount'].sum().sort_values(ascending=False).head(10) / 1000

fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(x=top_products.values, y=top_products.index, palette='crest', ax=ax)
ax.set_title("Top 10 Best-Selling Products by Revenue", fontsize=14, pad=15, fontweight='bold')
ax.set_xlabel("Total Sales (£ Thousands)", fontsize=11)
ax.set_ylabel("Product Description", fontsize=11)
for i, v in enumerate(top_products.values):
    ax.text(v + 2, i, f"£{v:.1f}K", va='center', fontsize=9, fontweight='bold')
plt.tight_layout()
fig.savefig(f"{output_dir}/03_top_products_revenue.png", dpi=200)
plt.close(fig)

# 4. Customer Repeat vs One-Time Breakdown
order_counts = df.groupby('CustomerID')['InvoiceNo'].nunique()
repeat_status = pd.Series({
    'Repeat Customers (>1 order)': (order_counts > 1).sum(),
    'One-Time Customers (1 order)': (order_counts == 1).sum()
})

fig, ax = plt.subplots(figsize=(7, 5))
colors = ['#2ca02c', '#ff7f0e']
wedges, texts, autotexts = ax.pie(
    repeat_status, labels=repeat_status.index, autopct='%1.1f%%',
    startangle=140, colors=colors, explode=(0.05, 0), textprops={'fontsize': 11}
)
plt.setp(autotexts, size=11, weight="bold", color="white")
ax.set_title("Customer Retention Profile (Repeat vs One-Time Buyers)", fontsize=13, pad=15, fontweight='bold')
plt.tight_layout()
fig.savefig(f"{output_dir}/04_customer_retention.png", dpi=200)
plt.close(fig)

print("All 4 presentation-ready charts successfully generated in:", output_dir)
