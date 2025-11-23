BEGIN;

-- Assume we're transferring funds between users
UPDATE accounts SET balance = balance - 50 WHERE user_id = 1; 
UPDATE accounts SET balance = balance + 50 WHERE user_id = 2;

COMMIT;
