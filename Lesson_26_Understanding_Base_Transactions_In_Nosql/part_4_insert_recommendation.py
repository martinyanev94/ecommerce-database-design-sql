def insert_recommendation(user_id, product_id):
    query = "INSERT INTO recommendations (user_id, product_id) VALUES (%s, %s)"
    session.execute(query, (user_id, product_id))
    print(f"Inserted recommendation for user {user_id} for product {product_id}")

# Simulate inserting a recommendation
insert_recommendation(1, 42)
