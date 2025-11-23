def insert_comment(user_id, comment_text):
    timestamp = datetime.datetime.now()
    query = "INSERT INTO comments (user_id, comment_text, timestamp) VALUES (%s, %s, %s)"
    session.execute(query, (user_id, comment_text, timestamp))
    print(f"Inserted comment for user {user_id} at {timestamp}")

# Simulating inserting a comment
insert_comment(2, 'This is a great product!')
