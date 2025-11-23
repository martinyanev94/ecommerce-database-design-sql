CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    shipping_address TEXT,
    version INT
);

-- Updating the order with a new version
UPDATE orders SET shipping_address = '987 Another Street', version = version + 1 WHERE order_id = 1;
