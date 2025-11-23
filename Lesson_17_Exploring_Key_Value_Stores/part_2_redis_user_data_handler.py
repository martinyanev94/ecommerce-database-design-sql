import redis

# Connect to Redis
client = redis.StrictRedis(host='localhost', port=6379, db=0)

# Set a value
client.set('user:user123', '{"age": 30, "email": "user123@example.com"}')

# Get the value
user_data = client.get('user:user123')
print(user_data.decode('utf-8'))
