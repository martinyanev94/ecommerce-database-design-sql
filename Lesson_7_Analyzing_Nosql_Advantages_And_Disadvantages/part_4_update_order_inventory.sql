BEGIN;
UPDATE inventory SET quantity = quantity - 1 WHERE product_id = 'A123';
INSERT INTO orders (user_id, product_id) VALUES ('456', 'A123');
COMMIT;
