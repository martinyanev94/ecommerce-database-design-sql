def route_to_shard(user_id):
    shard_id = hash(user_id) % number_of_shards
    return f"Routing to shard {shard_id}"

# Example usage
number_of_shards = 4
user_id = "user:1001"
print(route_to_shard(user_id))
