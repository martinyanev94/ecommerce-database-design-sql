import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('accounts')

response = table.update_item(
    Key={
        'account_id': 1
    },
    UpdateExpression='SET balance = :val',
    ExpressionAttributeValues={
        ':val': 500
    },
    ReturnValues='UPDATED_NEW'
)
