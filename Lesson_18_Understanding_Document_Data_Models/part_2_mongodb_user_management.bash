pip install pymongo
from pymongo import MongoClient

# Create a connection to the MongoDB database
client = MongoClient('mongodb://localhost:27017/')

# Create or access a database called 'mydatabase'
db = client['mydatabase']

# Create or access a collection called 'users'
users_collection = db['users']

# Insert a document into the users collection
new_user = {
    "user_id": "user123",
    "name": "John Doe",
    "email": "john.doe@example.com",
    "addresses": [
        {
            "type": "home",
            "line1": "123 Elm Street",
            "city": "Springfield",
            "zip": "12345"
        },
        {
            "type": "work",
            "line1": "456 Oak Avenue",
            "city": "Springfield",
            "zip": "12345"
        }
    ]
}

# Insert the user document
users_collection.insert_one(new_user)

# Retrieve the document
retrieved_user = users_collection.find_one({"user_id": "user123"})
print(retrieved_user)
