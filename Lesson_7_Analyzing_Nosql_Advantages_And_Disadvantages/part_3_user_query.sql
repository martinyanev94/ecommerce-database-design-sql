SELECT * FROM users WHERE user_id = '12345';
user = db.users.find_one({"user_id": "12345"})
