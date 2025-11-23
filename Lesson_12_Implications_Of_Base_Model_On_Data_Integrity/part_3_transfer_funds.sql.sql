BEGIN;
SET @current_balance = (SELECT balance FROM Accounts WHERE account_id = 1001);
IF @current_balance >= @transfer_amount THEN
    UPDATE Accounts SET balance = @current_balance - @transfer_amount WHERE account_id = 1001;
    COMMIT;
ELSE 
    ROLLBACK;
END IF;
