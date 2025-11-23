import boto3

def update_balance(user_id, new_balance):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Accounts')

    table.put_item(
        Item={
            'user_id': user_id,
            'balance': new_balance
        }
    )
    print(f"Balance for user {user_id} updated to {new_balance}.")
