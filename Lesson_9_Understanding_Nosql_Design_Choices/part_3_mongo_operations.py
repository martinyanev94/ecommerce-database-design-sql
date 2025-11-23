from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client.mydatabase
collection = db.mycollection

# Inserting new data
collection.insert_one({"username": "user1", "email": "user1@example.com"})

# Querying data
user = collection.find_one({"username": "user1"})
print(user)  # Output will show the stored user info
