import boto3

def save_profile(username, profile_data):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('user_profiles')

    response = table.put_item(
        Item={
            'username': username,
            'profile_data': profile_data
        }
    )
    print(f"Profile for {username} saved successfully.")

# Example usage
save_profile('john_doe', '{"age": 30, "city": "New York"}')
