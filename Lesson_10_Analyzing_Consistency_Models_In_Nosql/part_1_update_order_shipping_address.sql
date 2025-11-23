BEGIN;

-- Acquire a lock
LOCK TABLE orders IN EXCLUSIVE MODE;

-- Update operation
UPDATE orders SET shipping_address = '123 New Street' WHERE order_id = 1;

COMMIT;
