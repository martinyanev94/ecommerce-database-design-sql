from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('localhost', 27017)
db = client['your_database']
collection = db['users']

# Insert a user document
collection.insert_one({
    'user_id': 'some_user_id',
    'last_login': datetime.datetime.now()
})
