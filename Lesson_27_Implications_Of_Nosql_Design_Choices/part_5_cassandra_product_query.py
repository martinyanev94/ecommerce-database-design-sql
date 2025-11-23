from cassandra.cluster import Cluster

cluster = Cluster(['127.0.0.1'])
session = cluster.connect('my_keyspace')

def get_product(product_id, consistency_level):
    session.default_consistency_level = consistency_level
    query = "SELECT available_quantity FROM products WHERE product_id = %s"
    result = session.execute(query, (product_id,))
    return result

# Let's attempt to get product info with a lower consistency level
product_info = get_product(123, 'ONE')
print(f"Product available quantity: {product_info}")
