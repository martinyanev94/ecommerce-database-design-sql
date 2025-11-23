SELECT customer_id, COUNT(order_id) AS purchase_count
FROM orders
WHERE order_date > NOW() - INTERVAL '30 days'
GROUP BY customer_id
ORDER BY purchase_count DESC;
