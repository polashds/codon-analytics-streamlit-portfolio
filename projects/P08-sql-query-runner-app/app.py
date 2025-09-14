'''
-- Total revenue per region
SELECT region, SUM(revenue) AS total_revenue
FROM sales_data
GROUP BY region
ORDER BY total_revenue DESC;'''