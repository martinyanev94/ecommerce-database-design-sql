def update_price(product_id, new_price):
    while True:
        product = db.products.find_one({"_id": product_id})
        original_price = product["price"]
        
        if db.products.update_one(
            {"_id": product_id, "price": original_price},
            {"$set": {"price": new_price}}
        ).modified_count:
            print("Price updated successfully!")
            break
        else:
            print("Conflict detected, retrying...")
