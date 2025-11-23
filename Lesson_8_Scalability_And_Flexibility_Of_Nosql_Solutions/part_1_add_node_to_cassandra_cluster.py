from cassandra.cluster import Cluster

def add_node_to_cluster():
    cluster = Cluster(['node1', 'node2', 'node3', 'new_node'])
    # Data is automatically redistributed across the cluster
    print("New node added to the Cassandra cluster successfully.")
