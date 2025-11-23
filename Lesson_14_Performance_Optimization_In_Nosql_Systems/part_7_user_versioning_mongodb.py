from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
collection = db['users']

# Retrieve the current user state
current_user = collection.find_one({"name": "Alice"})

# Create a new version instead of updating
new_user_version = {
    "_id": current_user["_id"],
    "name": current_user["name"],
    "age": current_user["age"] + 1,  # Increment age
    "previous_versions": [current_user]  # Store the old state
}
collection.insert_one(new_user_version)
