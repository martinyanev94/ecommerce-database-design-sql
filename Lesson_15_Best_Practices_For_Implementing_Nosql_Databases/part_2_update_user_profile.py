from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
user_collection = db['users']

# Current user profile
user_id = "12345"
current_user = user_collection.find_one({"user_id": user_id})

# Update the profile with a new version
updated_user = {
    "user_id": user_id,
    "name": "Alice",
    "email": "alice@example.com",
    "age": current_user["age"] + 1,
    "version": current_user["version"] + 1
}
user_collection.update_one({"user_id": user_id}, {"$set": updated_user})
