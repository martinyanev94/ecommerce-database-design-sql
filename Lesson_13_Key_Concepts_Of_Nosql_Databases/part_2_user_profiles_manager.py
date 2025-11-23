user_profiles = {
    "user123": {"name": "Alice", "age": 30, "email": "alice@example.com"},
    "user456": {"name": "Bob", "age": 25, "email": "bob@example.com"},
}
def get_user_profile(user_id):
    return user_profiles.get(user_id, "User not found.")

print(get_user_profile("user123"))
