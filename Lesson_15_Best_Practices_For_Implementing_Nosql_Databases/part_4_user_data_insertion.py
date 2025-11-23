user = {
    "user_id": "12345",
    "name": "Alice",
    "orders": [
        {"order_id": "order-1", "amount": 100},
        {"order_id": "order-2", "amount": 150}
    ]
}

user_collection.insert_one(user)
