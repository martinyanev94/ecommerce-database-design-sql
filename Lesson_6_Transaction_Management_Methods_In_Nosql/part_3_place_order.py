import boto3

def place_order(user_id, order_id, order_data):
    dynamodb = boto3.resource('dynamodb')
    orders_table = dynamodb.Table('Orders')

    try:
        response = orders_table.put_item(
            Item={
                'order_id': order_id,
                'user_id': user_id,
                'order_data': order_data
            },
            ConditionExpression='attribute_not_exists(order_id)'  # Ensure we're not overwriting an existing order
        )
        print(f"Order {order_id} placed successfully.")

    except Exception as e:
        print(f"Failed to place order: {e}")
