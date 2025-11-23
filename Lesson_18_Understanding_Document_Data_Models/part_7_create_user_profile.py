def create_user_profile(user_data):
    validate_user_data(user_data)
    users_collection.insert_one(user_data)

# Dynamic user profile example
dynamic_profile = {
    "user_id": "user456",
    "name": "Jane Smith",
    "preferences": {
        "theme": "dark",
        "notifications": "enabled"
    },
    "posts": [],
}

create_user_profile(dynamic_profile)
