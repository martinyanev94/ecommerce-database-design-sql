BEGIN;

-- Check the balance first
SELECT balance FROM accounts WHERE user_id = 1 FOR UPDATE;

-- Update balance accordingly
UPDATE accounts SET balance = balance - 100 WHERE user_id = 1;

COMMIT;
