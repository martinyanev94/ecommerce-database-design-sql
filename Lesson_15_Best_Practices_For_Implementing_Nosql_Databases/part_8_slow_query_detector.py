import logging

logging.basicConfig(level=logging.INFO)

def execute_query(query):
    import time
    start_time = time.time()
    
    # Simulate querying the database
    time.sleep(0.6)  # Simulate a latency of 0.6 seconds
    end_time = time.time()
    
    if end_time - start_time > 0.5:
        logging.warning(f"Slow query detected: {query}")

execute_query("SELECT * FROM products WHERE price < 100")
