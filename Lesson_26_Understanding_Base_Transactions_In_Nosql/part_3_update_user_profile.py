from cassandra.cluster import Cluster

# Connect to the Cassandra cluster
cluster = Cluster(['127.0.0.1'])
session = cluster.connect('my_keyspace')

# Updating user profile
def update_user_profile(user_id, new_email):
    query = "UPDATE users SET email = %s WHERE user_id = %s"
    session.execute(query, (new_email, user_id))
    print(f"User {user_id} updated with new email: {new_email}")

# Perform an update
update_user_profile(1, 'new_email@example.com')
