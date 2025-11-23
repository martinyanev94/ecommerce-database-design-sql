BEGIN TRANSACTION;
INSERT INTO user_profiles (user_id, name, email) 
VALUES ('5678', 'Bob', 'bob@example.com');
COMMIT;
