-- DISPLAY ALL --
query1 = "SELECT COUNT(*) AS total_rows FROM retail_sales"
print(pd.read_sql(query1, conn))



-- KPI SUMMARY --
SELECT
    ROUND(SUM(sales), 2)                          AS total_revenue,
    ROUND(SUM(profit), 2)                         AS total_profit,
    ROUND(SUM(profit) * 100.0 / SUM(sales), 2)   AS profit_margin_pct,
    COUNT(DISTINCT order_id)                      AS total_orders,
    ROUND(AVG(sales), 2)                          AS avg_order_value
FROM retail_sales



-- REGIONAL ANALYSIS --
SELECT 
    region,
    ROUND(SUM(sales), 2)                          AS total_sales,
    ROUND(SUM(profit), 2)                         AS total_profit,
    ROUND(SUM(profit) * 100.0 / SUM(sales), 2)    AS profit_margin_pct,
    ROUND(AVG(discount) * 100, 1)                 AS avg_discount_pct
FROM retail_sales
GROUP BY region
ORDER BY profit_margin_pct ASC;


-- LEAKAGE ANALYSIS --
SELECT
    region,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(sales) * 100.0 / (SELECT SUM(sales) FROM retail_sales), 2) AS pct_of_total
FROM retail_sales
WHERE region IN ('Southwest', 'Central', 'South')
GROUP BY region


-- SALES BY CATEGORY --
SELECT 
    category,
    ROUND(SUM(sales), 2)                          AS total_sales,
    ROUND(SUM(profit), 2)                         AS total_profit,
    ROUND(SUM(profit) * 100.0 / SUM(sales), 2)    AS profit_margin_pct
FROM retail_sales
GROUP BY category
ORDER BY total_sales DESC;


-- CUSTOMER SEGMENT ANALYSIS --
SELECT
    customer_segment,
    ROUND(SUM(sales), 2)                        AS total_sales,
    ROUND(SUM(profit), 2)                       AS total_profit,
    ROUND(SUM(profit) * 100.0 / SUM(sales), 2)  AS profit_margin_pct,
    ROUND(AVG(sales), 2)                        AS avg_order_value
FROM retail_sales
GROUP BY customer_segment
ORDER BY total_sales DESC;
