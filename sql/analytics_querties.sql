
SELECT 
    COUNT(DISTINCT "InvoiceNo") AS total_orders,
    COUNT(DISTINCT "CustomerID") AS total_customers,
    ROUND(SUM("TotalAmount")::numeric, 2) AS total_revenue,
    ROUND(AVG("TotalAmount")::numeric, 2) AS avg_item_value
FROM sales_transactions;

-- 2. Monthly Revenue Trend
SELECT 
    TO_CHAR("InvoiceDate", 'YYYY-MM') AS sales_month,
    COUNT(DISTINCT "InvoiceNo") AS total_orders,
    ROUND(SUM("TotalAmount")::numeric, 2) AS monthly_revenue
FROM sales_transactions
GROUP BY sales_month
ORDER BY sales_month;

-- 3. Top 10 Revenue-Generating Products
SELECT 
    "Description",
    SUM("Quantity") AS total_units_sold,
    ROUND(SUM("TotalAmount")::numeric, 2) AS product_revenue
FROM sales_transactions
GROUP BY "Description"
ORDER BY product_revenue DESC
LIMIT 10;

-- 4. Top 10 Countries by Revenue
SELECT 
    "Country",
    COUNT(DISTINCT "CustomerID") AS unique_customers,
    ROUND(SUM("TotalAmount")::numeric, 2) AS country_revenue
FROM sales_transactions
GROUP BY "Country"
ORDER BY country_revenue DESC
LIMIT 10;