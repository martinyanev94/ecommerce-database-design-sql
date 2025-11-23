from couchbase.cluster import Cluster, ClusterOptions
from couchbase_core.cluster import PasswordAuthenticator

def submit_payment(user_id, amount):
    cluster = Cluster('couchbase://localhost', ClusterOptions(
        PasswordAuthenticator('username', 'password')))
    bucket = cluster.bucket('payments_bucket')

    payment_doc = {
        'user_id': user_id,
        'amount': amount
    }

    bucket.default_collection().upsert(f'payment_{user_id}', payment_doc, 
                                        couchbase.kv.UpsertOptions().durability(durability='majority'))
    print(f"Payment of {amount} submitted for user {user_id}.")

# Example usage
submit_payment('user456', 100)
