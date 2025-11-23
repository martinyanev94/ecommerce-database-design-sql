import redis

# Connect to Redis
cache = redis.StrictRedis(host='localhost', port=6379, db=0)

# Cache a comment
cache.set('comment_12345', 'This is awesome!')
