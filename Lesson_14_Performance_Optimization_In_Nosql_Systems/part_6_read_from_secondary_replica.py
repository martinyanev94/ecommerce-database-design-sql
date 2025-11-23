# Read from a secondary replica
secondary_client = MongoClient('mongodb://secondary_host:27017/?replicaSet=myReplicaSet')
db = secondary_client['mydatabase']
collection = db['users']

# Retrieve data from the secondary
result = collection.find_one({"name": "Alice"})
print(result)
