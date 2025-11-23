from couchbase.bucket import Bucket
from couchbase.exceptions import DocumentNotFoundException

# Connect to Couchbase
bucket = Bucket('couchbase://localhost/mybucket')

# Insert a document with eventual consistency
bucket.insert('user:1000', {"name": "Alice", "age": 30}, persist_to=0, replicate_to=0)

# Try to fetch the document (might not be available yet)
try:
    user = bucket.get('user:1000')
    print(user.value)
except DocumentNotFoundException:
    print("Document not found immediately; it may take some time to replicate.")
