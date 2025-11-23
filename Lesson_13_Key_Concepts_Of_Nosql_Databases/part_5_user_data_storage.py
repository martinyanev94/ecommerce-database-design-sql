from collections import defaultdict

column_family = defaultdict(lambda: defaultdict(dict))

# Storing data
column_family["user:123"]["personal"]["name"] = "Alice"
column_family["user:123"]["personal"]["age"] = 30
column_family["user:123"]["contacts"]["email"] = "alice@example.com"

# Retrieving data
user_id = "user:123"
def get_user_data(user_id):
    return dict(column_family[user_id])

print(get_user_data(user_id))
