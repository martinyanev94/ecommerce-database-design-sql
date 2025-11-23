from pymongo import MongoClient

def place_order(order_id, order_details):
    client = MongoClient('mongodb://localhost:27017/')
    db = client['orders_db']
    orders_collection = db['orders']

    order_document = {
        'order_id': order_id,
        'order_details': order_details
    }

    # Inserts the order and waits for the primary acknowledgment
    orders_collection.insert_one(order_document)
    print(f"Order {order_id} placed successfully.")

# Example usage
place_order('order789', '{"item": "Laptop", "quantity": 1}')
