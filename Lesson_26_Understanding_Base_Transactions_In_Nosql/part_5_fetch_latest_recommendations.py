def get_latest_recommendations(user_id):
    query = "SELECT product_id FROM recommendations WHERE user_id = %s"
    rows = session.execute(query, (user_id,))
    return [row.product_id for row in rows]

# Fetch recommendations
latest_recommendations = get_latest_recommendations(1)
print(f"Latest recommendations for user 1: {latest_recommendations}")
