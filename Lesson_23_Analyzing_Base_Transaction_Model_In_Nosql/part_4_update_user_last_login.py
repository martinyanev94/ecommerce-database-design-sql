from cassandra.cluster import Cluster

# Connect to a Cassandra cluster
cluster = Cluster(['127.0.0.1'])
session = cluster.connect('your_keyspace')

# Update user last login
session.execute(
    """
    UPDATE users 
    SET last_login = now() 
    WHERE user_id = some_user_id
    """
)
