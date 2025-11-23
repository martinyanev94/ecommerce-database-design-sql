CREATE KEYSPACE IF NOT EXISTS retail WITH REPLICATION = {
  'class': 'SimpleStrategy',
  'replication_factor': 3
};

CREATE TABLE IF NOT EXISTS retail.orders (
    order_id UUID PRIMARY KEY,
    item_name TEXT,
    quantity INT,
    order_date TIMESTAMP
);

INSERT INTO retail.orders (order_id, item_name, quantity, order_date)
VALUES (uuid(), 'Laptop', 2, '2023-06-01 10:00:00');
