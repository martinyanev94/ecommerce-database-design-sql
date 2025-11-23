import redis

# Connect to Redis
client = redis.StrictRedis(host='localhost', port=6379, db=0)

# Set a value
client.set('user:1000', 'Alice')

# Get the value
user_name = client.get('user:1000')
print(f"User ID 1000 is {user_name.decode('utf-8')}")
