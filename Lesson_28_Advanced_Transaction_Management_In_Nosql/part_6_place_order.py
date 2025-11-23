def place_order(user_id, order_data):
    session = client.start_session()
    try:
        session.start_transaction()

        # Check inventory
        inventory_item = db.inventory.find_one({"_id": order_data["item_id"]})
        if inventory_item["stock"] >= order_data["quantity"]:
            db.inventory.update_one(
                {"_id": order_data["item_id"]},
                {"$inc": {"stock": -order_data["quantity"]}},
                session=session
            )
            # Create the order
            db.orders.insert_one(order_data, session=session)
            session.commit_transaction()
            print("Order placed successfully!")
        else:
            print("Not enough stock available.")
            session.abort_transaction()
    except Exception as e:
        session.abort_transaction()
        print(f"Order could not be placed: {e}")
    finally:
        session.end_session()
