from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]

session = client.start_session()

transaction = [
    {"$set": {"quantity": 50}}, 
    {"$set": {"quantity": 30}}
]

try:
    session.start_transaction()
    
    db.collection1.update_one({"product_id": 1}, transaction[0], session=session)
    db.collection2.update_one({"product_id": 2}, transaction[1], session=session)
    
    session.commit_transaction()
    print("Transaction committed successfully!")
except Exception as e:
    session.abort_transaction()
    print(f"Transaction aborted due to: {e}")
finally:
    session.end_session()
