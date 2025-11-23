from pymongo import MongoClient
from pymongo import WriteConcern

client = MongoClient('mongodb://localhost:27017/')
session = client.start_session()

with session.start_transaction():
    db.accounts.update_one({'user_id': 'user_123'}, {'$inc': {'balance': -100}}, session=session)
    db.accounts.update_one({'user_id': 'user_456'}, {'$inc': {'balance': 100}}, session=session)
