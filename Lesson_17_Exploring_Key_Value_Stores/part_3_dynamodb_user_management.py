# Using DynamoDB to set an item
import boto3

# Create a DynamoDB client
dynamodb = boto3.resource('dynamodb')

# Table reference
table = dynamodb.Table('Users')

# Add a new user
table.put_item(
    Item={
        'username': 'user123',
        'details': {'age': 30, 'email': 'user123@example.com'}
    }
)

# Get the user data
response = table.get_item(
    Key={'username': 'user123'}
)
print(response['Item'])
