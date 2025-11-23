# Update user document to include phone_numbers array
users_collection.update_one(
    {"user_id": "user123"},
    {
        "$set": {
            "phone_numbers": [
                {"type": "mobile", "number": "123-456-7890"},
                {"type": "home", "number": "098-765-4321"}
            ]
        }
    }
)

# Retrieve the updated document
updated_user = users_collection.find_one({"user_id": "user123"})
print(updated_user)
