CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    details JSONB
);

INSERT INTO users (username, details)
VALUES 
    ('user123', '{"age": 30, "email": "user123@example.com"}');
