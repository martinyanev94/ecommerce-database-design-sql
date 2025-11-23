SELECT users.username, orders.product_id
FROM users
JOIN orders ON users.user_id = orders.user_id
WHERE users.username = 'user123';
