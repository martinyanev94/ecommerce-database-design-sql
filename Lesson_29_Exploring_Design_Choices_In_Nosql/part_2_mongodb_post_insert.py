from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["social_media"]

# User post data
post = {
    "user_id": 1,
    "content": "Just enjoying the sunny weather!",
    "timestamp": datetime.now()
}

# Insert post into the database
result = db.posts.insert_one(post)
print(f"Post created with ID: {result.inserted_id}")
