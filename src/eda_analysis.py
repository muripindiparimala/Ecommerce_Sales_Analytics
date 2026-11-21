"""
Exploratory Data Analysis (EDA) Module
Project: E-Commerce Sales Analytics
Author: EduSkills Internship Team
"""

import pandas as pd
import numpy as np

def run_eda(file_path: str = "data/processed/cleaned_online_retail.csv"):
    print("=" * 60)
    print("E-COMMERCE SALES ANALYTICS - EXPLORATORY DATA ANALYSIS (EDA)")
    print("=" * 60)

    # 1. Load Cleaned Dataset
    df = pd.read_csv(file_path)
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

    print(f"\n[1] DATASET OVERVIEW")
    print(f"Total Transactions (Rows): {len(df):,}")
    print(f"Total Attributes (Columns): {df.shape[1]}")
    print(f"Memory Usage: {df.memory_usage().sum() / (1024*1024):.2f} MB")
    print(f"Missing Values: {df.isnull().sum().sum()}")

    # 2. Executive KPIs
    total_revenue = df['TotalAmount'].sum()
    total_orders = df['InvoiceNo'].nunique()
    total_customers = df['CustomerID'].nunique()
    total_products = df['StockCode'].nunique()
    aov = total_revenue / total_orders
    items_per_order = df.groupby('InvoiceNo')['Quantity'].sum().mean()
    min_date = df['InvoiceDate'].min()
    max_date = df['InvoiceDate'].max()

    print(f"\n[2] EXECUTIVE BUSINESS KPIS")
    print(f"- Total Revenue: £{total_revenue:,.2f}")
    print(f"- Total Unique Orders: {total_orders:,}")
    print(f"- Total Unique Customers: {total_customers:,}")
    print(f"- Total Unique Products (SKUs): {total_products:,}")
    print(f"- Average Order Value (AOV): £{aov:.2f}")
    print(f"- Average Items Per Order: {items_per_order:.1f} units")
    print(f"- Analysis Period: {min_date.strftime('%Y-%m-%d')} to {max_date.strftime('%Y-%m-%d')} ({(max_date - min_date).days} days)")

    # 3. Monthly Sales Performance
    df['YearMonth'] = df['InvoiceDate'].dt.to_period('M')
    monthly_sales = df.groupby('YearMonth').agg(
        Revenue=('TotalAmount', 'sum'),
        Orders=('InvoiceNo', 'nunique'),
        ActiveCustomers=('CustomerID', 'nunique')
    ).reset_index()
    monthly_sales['Monthly_Growth_Pct'] = monthly_sales['Revenue'].pct_change() * 100

    print(f"\n[3] MONTHLY SALES PERFORMANCE")
    print(monthly_sales.to_string(index=False, formatters={
        'Revenue': '£{:,.2f}'.format,
        'Orders': '{:,}'.format,
        'ActiveCustomers': '{:,}'.format,
        'Monthly_Growth_Pct': '{:+.2f}%'.format
    }))

    # 4. Geographic Analysis (Top 10 Countries)
    country_summary = df.groupby('Country').agg(
        Revenue=('TotalAmount', 'sum'),
        Orders=('InvoiceNo', 'nunique'),
        Customers=('CustomerID', 'nunique')
    ).sort_values('Revenue', ascending=False)
    country_summary['Revenue_Share_Pct'] = (country_summary['Revenue'] / total_revenue) * 100

    print(f"\n[4] TOP 10 COUNTRIES BY REVENUE")
    print(country_summary.head(10).to_string(formatters={
        'Revenue': '£{:,.2f}'.format,
        'Orders': '{:,}'.format,
        'Customers': '{:,}'.format,
        'Revenue_Share_Pct': '{:.2f}%'.format
    }))

    # 5. Top 10 Best-Selling Products by Revenue
    top_rev_products = df.groupby(['StockCode', 'Description']).agg(
        Revenue=('TotalAmount', 'sum'),
        UnitsSold=('Quantity', 'sum'),
        OrderCount=('InvoiceNo', 'nunique')
    ).sort_values('Revenue', ascending=False).reset_index()

    print(f"\n[5] TOP 10 PRODUCTS BY REVENUE")
    print(top_rev_products.head(10).to_string(index=False, formatters={
        'Revenue': '£{:,.2f}'.format,
        'UnitsSold': '{:,}'.format,
        'OrderCount': '{:,}'.format
    }))

    # 6. Customer Concentration (Pareto 80/20 Rule)
    customer_rev = df.groupby('CustomerID')['TotalAmount'].sum().sort_values(ascending=False).reset_index()
    top_20_count = int(len(customer_rev) * 0.20)
    top_20_revenue = customer_rev.head(top_20_count)['TotalAmount'].sum()
    top_10_count = int(len(customer_rev) * 0.10)
    top_10_revenue = customer_rev.head(top_10_count)['TotalAmount'].sum()

    print(f"\n[6] CUSTOMER CONCENTRATION (PARETO PRINCIPLE)")
    print(f"- Top 10% Customers ({top_10_count:,} accounts) generate: £{top_10_revenue:,.2f} ({(top_10_revenue/total_revenue)*100:.2f}% of total sales)")
    print(f"- Top 20% Customers ({top_20_count:,} accounts) generate: £{top_20_revenue:,.2f} ({(top_20_revenue/total_revenue)*100:.2f}% of total sales)")

    # 7. Customer Order Frequency (Repeat vs One-Time)
    order_counts = df.groupby('CustomerID')['InvoiceNo'].nunique()
    one_time_buyers = (order_counts == 1).sum()
    repeat_buyers = (order_counts > 1).sum()

    print(f"\n[7] CUSTOMER RETENTION PROFILE")
    print(f"- One-Time Buyers: {one_time_buyers:,} ({(one_time_buyers / total_customers)*100:.2f}%)")
    print(f"- Repeat Buyers: {repeat_buyers:,} ({(repeat_buyers / total_customers)*100:.2f}%)")
    print(f"- Maximum Orders by Single Customer: {order_counts.max():,} orders")

    # 8. Transaction Distribution Stats
    print(f"\n[8] NUMERICAL DISTRIBUTION METRICS")
    num_stats = df[['Quantity', 'UnitPrice', 'TotalAmount']].describe(percentiles=[0.25, 0.50, 0.75, 0.90, 0.99]).round(2)
    print(num_stats.to_string())

    print("\n" + "=" * 60)
    print("EDA EXECUTION COMPLETED")
    print("=" * 60)

if __name__ == "__main__":
    run_eda()
