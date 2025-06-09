import boto3
import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

s3 = boto3.client("s3")
sns = boto3.client("sns")

TOPIC_ARN = "arn:"
BUCKET_NAME = "bucket_name"

def lambda_handler(event, context):
    for record in event["Records"]:
        try:
            new_image = record["dynamodb"]["NewImage"]

            order = {
                "orderId": new_image["orderID"]["S"], 
                "user": new_image["user"]["S"],
                "product": new_image["product"]["S"],
                "quantity": int(new_image["quantity"]["N"]),
                "timestamp": new_image["timestamp"]["S"],
            }

            s3.put_object(
                Bucket=BUCKET_NAME,
                Key=f"orders/{order['orderId']}.json",
                Body=json.dumps(order)
            )
            logger.info(f"Stored order to S3: {order['orderId']}")

            sns.publish(
                TopicArn=TOPIC_ARN,
                Subject="New Order Received",
                Message=f"New order placed by {order['user']}:\n\n{json.dumps(order, indent=2)}"
            )
            logger.info(f"Notification sent for order: {order['orderId']}")

        except Exception as e:
            logger.error("Error processing record:")
            logger.exception(e)
