def validate_user_data(user_data):
    required_fields = ['user_id', 'name', 'email']
    for field in required_fields:
        if field not in user_data:
            raise ValueError(f'Missing required field: {field}')
    # Additional validation logic can be added here

# Example user data
new_user_data = {
    "user_id": "user123",
    "name": "John Doe",
    "email": "john.doe@example.com"
}

# Validate before inserting
try:
    validate_user_data(new_user_data)
    users_collection.insert_one(new_user_data)
except ValueError as e:
    print(e)
