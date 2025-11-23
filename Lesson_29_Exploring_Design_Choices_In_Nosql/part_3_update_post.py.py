# Update post with potential conflicts
update_query = {"user_id": 1, "content": "New update!"}
result = db.posts.update_one(
    {"user_id": 1},
    {"$set": {"content": update_query["content"], "timestamp": datetime.now()}}
)

if result.modified_count:
    print("Post updated successfully!")
else:
    print("No updates were made.")
