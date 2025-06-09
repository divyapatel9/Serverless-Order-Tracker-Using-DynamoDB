import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Orders')

def lambda_handler(event, context):
    print("Incoming Event:", event)

    try:
        body = json.loads(event['body'])
        print("Parsed Body:", body)

        order_id = body['orderId']
        user = body['user']
        product = body['product']
        quantity = int(body['quantity'])
        timestamp = body['timestamp']

        table.put_item(
            Item={
                'orderID': order_id, 
                'user': user,
                'product': product,
                'quantity': quantity,
                'timestamp': timestamp
            }
        )

        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Order saved successfully!'})
        }

    except Exception as e:
        print("Error:", str(e))
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
