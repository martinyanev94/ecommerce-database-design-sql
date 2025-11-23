def shard_user(user_id):
    shard_id = hash(user_id) % number_of_shards
    return f"Routing to shard {shard_id}"

number_of_shards = 4
user_id = "user-456"
print(shard_user(user_id))
