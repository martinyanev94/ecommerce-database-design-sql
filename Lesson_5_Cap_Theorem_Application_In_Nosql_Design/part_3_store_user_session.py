from cassandra.cluster import Cluster

def store_session(user_id, session_data):
    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect('session_keyspace')

    # Using a simple INSERT statement
    query = f"INSERT INTO user_sessions (user_id, session_data) VALUES ('{user_id}', '{session_data}')"
    session.execute(query)
    print(f"Session data for user {user_id} stored successfully.")

# Example usage
store_session('user123', '{"last_seen": "2023-10-01T12:00:00Z"}')
