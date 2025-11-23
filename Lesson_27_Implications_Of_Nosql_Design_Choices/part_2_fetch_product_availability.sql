SET TRANSACTION ISOLATION LEVEL READ COMMITTED;

SELECT product_id, available_quantity
FROM products
WHERE product_id = 123;
