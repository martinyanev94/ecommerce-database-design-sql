import redis

cache = redis.StrictRedis(host='localhost', port=6379, db=0)

def get_product(product_id):
    # First, check if the data is in cache
    cached_product = cache.get(product_id)
    if cached_product:
        return cached_product

    # Proceed to query the database
    product = product_collection.find_one({"product_id": product_id})
    # Cache the product
    cache.set(product_id, product)
    return product
