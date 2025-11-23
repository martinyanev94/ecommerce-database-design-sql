from couchbase.cluster import Cluster, ClusterOptions
from couchbase_core.cluster import PasswordAuthenticator

def update_profile(user_id, new_data):
    cluster = Cluster('couchbase://localhost', ClusterOptions(
        PasswordAuthenticator('admin', 'password')))
    bucket = cluster.bucket('user_profiles')
    collection = bucket.default_collection()

    user_doc = collection.get(user_id)

    new_profile_data = {**user_doc.content, **new_data}

    try:
        collection.upsert(user_id, new_profile_data, 
                          retry_strategy=couchbase.retry.RetryStrategy())
        print("Profile updated successfully.")

    except couchbase.exceptions.DocumentNotFound as e:
        print(f"Failed to update profile: {e}")
