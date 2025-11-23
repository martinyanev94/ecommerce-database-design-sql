-- SQL-style handling of a transaction
BEGIN;
INSERT INTO users (user_id, name) VALUES ('001', 'Alice');
COMMIT;
