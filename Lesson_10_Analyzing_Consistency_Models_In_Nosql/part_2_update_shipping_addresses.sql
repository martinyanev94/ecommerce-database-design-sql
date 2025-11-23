-- Background process to update shipping addresses
INSERT INTO shipping_updates (order_id, new_address) VALUES (1, '123 New Street');

-- Later process that applies updates asynchronously
UPDATE orders SET shipping_address = (SELECT new_address FROM shipping_updates WHERE order_id = 1) WHERE order_id = 1;
