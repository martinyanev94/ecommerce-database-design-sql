BEGIN;

-- Query ensuring a strong consistent read
SELECT * FROM orders WHERE order_id = 1 FOR UPDATE;

-- Update the order
UPDATE orders SET shipping_address = '456 Updated Avenue' WHERE order_id = 1;

COMMIT;
