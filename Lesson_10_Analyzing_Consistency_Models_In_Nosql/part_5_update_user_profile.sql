-- User session: updating profile
BEGIN;

UPDATE users SET email = 'new_email@example.com' WHERE user_id = 10;

SELECT * FROM users WHERE user_id = 10;

COMMIT;
