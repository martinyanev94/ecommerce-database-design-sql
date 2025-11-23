from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
collection = db['users']

# Insert a document
user = {"name": "Alice", "age": 30, "city": "New York"}
collection.insert_one(user)

# Query for the document
result = collection.find_one({"name": "Alice"})
print(result)
collection.create_index([("name", 1)])  # 1 for ascending order
