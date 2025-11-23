CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    category_name VARCHAR(50)
);

ALTER TABLE books
ADD COLUMN category_id INT,
ADD FOREIGN KEY (category_id) REFERENCES categories(id);
