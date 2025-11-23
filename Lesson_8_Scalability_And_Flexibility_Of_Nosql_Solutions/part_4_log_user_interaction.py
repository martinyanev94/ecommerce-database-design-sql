import boto3

def log_user_interaction(user_id, video_id):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('UserInteractions')
    
    table.put_item(
        Item={
            'user_id': user_id,
            'video_id': video_id,
            'timestamp': '2021-10-01T12:00:00Z'
        }
    )
    print(f"Logged interaction for user {user_id} and video {video_id}.")
