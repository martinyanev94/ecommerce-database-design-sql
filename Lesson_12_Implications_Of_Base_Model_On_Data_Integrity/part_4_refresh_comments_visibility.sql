-- Pseudo-code illustrating a refresh mechanism
WHILE true DO
    UPDATE comments SET visibility = "updated" WHERE visibility = "old" AND timestamp < CURRENT_TIMESTAMP - INTERVAL '5 minutes';
    SLEEP(60); -- Wait for 60 seconds before the next sync
END WHILE;
