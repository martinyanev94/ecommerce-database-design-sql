CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE user_product_views (
    user_id INT REFERENCES users(id),
    product_id INT REFERENCES products(id),
    PRIMARY KEY (user_id, product_id)
);
SELECT DISTINCT p.name
FROM user_product_views upv
JOIN users u ON upv.user_id = u.id
JOIN products p ON upv.product_id = p.id
WHERE u.id IN (SELECT f.user_id_b
                FROM friendships f
                WHERE f.user_id_a = (SELECT id FROM users WHERE name = 'Alice'))
AND p.id NOT IN (SELECT product_id FROM user_product_views WHERE user_id = (SELECT id FROM users WHERE name = 'Alice'));
