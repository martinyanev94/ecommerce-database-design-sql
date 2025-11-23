CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE friendships (
    user_id_a INT REFERENCES users(id),
    user_id_b INT REFERENCES users(id),
    PRIMARY KEY (user_id_a, user_id_b)
);
