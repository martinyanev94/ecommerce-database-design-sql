from pymongo import MongoClient

def create_user_profile(username, posts, friends):
    client = MongoClient('mongodb://localhost:27017/')
    db = client['social_media']
    user_profile = {
        'username': username,
        'posts': posts,
        'friends': friends
    }
    db.users.insert_one(user_profile)
    print(f"User profile for {username} created successfully.")
