import time
import logging

logging.basicConfig(level=logging.INFO)

def execute_query(query):
    start_time = time.time()
    # Simulate a database query
    # Here you would call your NoSQL database query function
    time.sleep(0.5)  # Simulating query execution time
    end_time = time.time()

    if end_time - start_time > 0.4:  # Threshold for slow query
        logging.warning(f"Slow query detected: {query}")

# Example of running a query
execute_query("SELECT * FROM users WHERE age > 30")
