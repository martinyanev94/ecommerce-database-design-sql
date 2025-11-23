CREATE TABLE accounts (
    id SERIAL PRIMARY KEY,
    account_number VARCHAR(20) NOT NULL
);

CREATE TABLE transactions (
    from_account_id INT REFERENCES accounts(id),
    to_account_id INT REFERENCES accounts(id),
    amount DECIMAL(10,2),
    transaction_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
SELECT from_account_id, to_account_id, COUNT(*) AS transaction_count
FROM transactions
GROUP BY from_account_id, to_account_id
HAVING COUNT(*) > 10; -- More than 10 transactions between the same accounts
