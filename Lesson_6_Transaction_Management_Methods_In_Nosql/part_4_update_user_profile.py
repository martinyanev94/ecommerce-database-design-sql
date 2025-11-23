from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement

def update_user_profile(user_id, new_profile_data):
    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect('user_profiles')

    query = SimpleStatement(
        f"UPDATE profiles SET profile_data = '{new_profile_data}' WHERE user_id = '{user_id}' IF EXISTS"
    )

    result = session.execute(query)

    if result.was_applied:
        print("User profile updated successfully.")
    else:
        print("User profile update failed: User does not exist.")
