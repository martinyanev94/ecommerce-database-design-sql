INSERT INTO users (name) VALUES ('Alice'), ('Bob'), ('Charlie');

INSERT INTO friendships (user_id_a, user_id_b) VALUES
(1, 2),  -- Alice is friends with Bob
(1, 3),  -- Alice is friends with Charlie
(2, 3);  -- Bob is friends with Charlie
SELECT u2.name
FROM friendships f
JOIN users u1 ON f.user_id_a = u1.id
JOIN users u2 ON f.user_id_b = u2.id
WHERE u1.name = 'Alice';
