import pandas as pd
pd.set_option('display.float_format', '{:,.2f}'.format)
import sqlite3

df = pd.read_csv('retail_sales_clean.csv')
conn = sqlite3.connect('retail_analytics.db')
df.to_sql('retail_sales', conn, index=False, if_exists='replace')

print("Database ready!")

query1 = "SELECT COUNT(*) AS total_rows FROM retail_sales"
print(pd.read_sql(query1, conn))




kpi_query = """
SELECT
    ROUND(SUM(sales), 2)                          AS total_revenue,
    ROUND(SUM(profit), 2)                         AS total_profit,
    ROUND(SUM(profit) * 100.0 / SUM(sales), 2)   AS profit_margin_pct,
    COUNT(DISTINCT order_id)                      AS total_orders,
    ROUND(AVG(sales), 2)                          AS avg_order_value
FROM retail_sales
"""
print("=== KPI SUMMARY ===")
print(pd.read_sql(kpi_query, conn))   




regional_analysis = """
SELECT 
    region,
    ROUND(SUM(sales), 2)                          AS total_sales,
    ROUND(SUM(profit), 2)                         AS total_profit,
    ROUND(SUM(profit) * 100.0 / SUM(sales), 2)    AS profit_margin_pct,
    ROUND(AVG(discount) * 100, 1)                 AS avg_discount_pct
FROM retail_sales
GROUP BY region
ORDER BY profit_margin_pct ASC;
"""
print(pd.read_sql(regional_analysis, conn))



leakage_query = """
SELECT
    region,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(sales) * 100.0 / (SELECT SUM(sales) FROM retail_sales), 2) AS pct_of_total
FROM retail_sales
WHERE region IN ('Southwest', 'Central', 'South')
GROUP BY region
"""
print("=== REVENUE LEAKAGE ===")
print(pd.read_sql(leakage_query, conn))



sales_by_category = """
SELECT 
    category,
    ROUND(SUM(sales), 2)                          AS total_sales,
    ROUND(SUM(profit), 2)                         AS total_profit,
    ROUND(SUM(profit) * 100.0 / SUM(sales), 2)    AS profit_margin_pct
FROM retail_sales
GROUP BY category
ORDER BY total_sales DESC;
"""
print("=====SALES BY CATEGORY=====")
print(pd.read_sql(sales_by_category, conn))



customer_segment_analysis = """
SELECT
    customer_segment,
    ROUND(SUM(sales), 2)                        AS total_sales,
    ROUND(SUM(profit), 2)                       AS total_profit,
    ROUND(SUM(profit) * 100.0 / SUM(sales), 2)  AS profit_margin_pct,
    ROUND(AVG(sales), 2)                        AS avg_order_value
FROM retail_sales
GROUP BY customer_segment
ORDER BY total_sales DESC;
"""
print("=====CUSTOMER SEGMENT ANALYSIS=====")
print(pd.read_sql(customer_segment_analysis, conn))