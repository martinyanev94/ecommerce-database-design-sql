import redis

# Connect to Redis
client = redis.StrictRedis(host='localhost', port=6379, db=0)

# Set a key-value pair
client.set('user:1000', '{"name": "Alice", "age": 30}')

# Retrieve the value
user_data = client.get('user:1000')
print(user_data)
