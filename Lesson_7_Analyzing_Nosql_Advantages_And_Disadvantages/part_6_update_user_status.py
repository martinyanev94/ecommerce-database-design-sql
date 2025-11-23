from cassandra.cluster import Cluster

def update_user_status(user_id, new_status):
    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect('user_data')

    query = f"UPDATE users SET status = '{new_status}' WHERE user_id = '{user_id}' IF EXISTS"
    result = session.execute(query)

    if result.was_applied:
        print("User status updated successfully.")
    else:
        print("Update failed: User does not exist.")
