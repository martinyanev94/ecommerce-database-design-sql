def validate_user_profile(username, posts, friends):
    if not isinstance(username, str) or len(username) < 3:
        raise ValueError("Invalid username. Must be at least 3 characters.")
    if not isinstance(posts, list) or not isinstance(friends, list):
        raise ValueError("Posts and friends must be lists.")
    print(f"User profile for {username} is valid.")

# Example usage
try:
    validate_user_profile("user1", [], [])
except ValueError as e:
    print(e)
