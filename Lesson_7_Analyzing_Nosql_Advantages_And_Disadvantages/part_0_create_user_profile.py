from pymongo import MongoClient

def create_user_profile(user_id, user_name, email):
    client = MongoClient('mongodb://localhost:27017/')
    db = client['user_profiles']
    
    db.profiles.insert_one({
        'user_id': user_id,
        'user_name': user_name,
        'email': email
    })
    print(f"User profile for {user_name} created successfully.")
