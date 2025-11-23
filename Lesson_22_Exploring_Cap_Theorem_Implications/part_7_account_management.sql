CREATE TABLE accounts (
    account_id SERIAL PRIMARY KEY,
    balance NUMERIC NOT NULL
);
UPDATE accounts
SET balance = balance - 100
WHERE account_id = 1;
