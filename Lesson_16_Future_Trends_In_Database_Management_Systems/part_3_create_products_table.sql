CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    specs JSONB
);

INSERT INTO products (name, specs)
VALUES 
    ('Smartphone', '{"screen": "6.1 inch", "battery": "4000mAh", "camera": "12MP"}'),
    ('Smartwatch', '{"screen": "1.2 inch", "battery": "200mAh", "features": ["heart rate", "GPS"]}');
