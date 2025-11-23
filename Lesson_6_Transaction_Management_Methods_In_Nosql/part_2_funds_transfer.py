from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, OperationFailure

def transfer_funds(sender_id, receiver_id, amount):
    client = MongoClient('mongodb://localhost:27017/')
    db = client['banking']
    
    session = client.start_session()
    session.start_transaction()

    try:
        sender_balance = db.accounts.find_one({"_id": sender_id}, session=session)
        receiver_balance = db.accounts.find_one({"_id": receiver_id}, session=session)

        if sender_balance['balance'] >= amount:
            db.accounts.update_one({"_id": sender_id}, {"$inc": {"balance": -amount}}, session=session)
            db.accounts.update_one({"_id": receiver_id}, {"$inc": {"balance": amount}}, session=session)
            session.commit_transaction()
            print("Transaction completed successfully.")
        else:
            print("Insufficient funds.")
            session.abort_transaction()

    except (ConnectionFailure, OperationFailure) as e:
        print(f"Transaction aborted due to error: {e}")
        session.abort_transaction()

    finally:
        session.end_session()
