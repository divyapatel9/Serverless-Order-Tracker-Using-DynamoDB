import requests
import json
import random
import time
import uuid
from datetime import datetime

url = "https://o9oksk3qg7.execute-api.us-east-2.amazonaws.com/prod/order"

products = ["Laptop", "Phone", "Mouse", "Headphones", "Monitor"]

headers = {
    "Content-Type": "application/json"
}

def generate_order():
    return {
        "orderId": str(uuid.uuid4()),  # unique ID
        "user": f"user{random.randint(1,100)}@example.com",
        "product": random.choice(products),
        "quantity": random.randint(1, 5),
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }

while True:
    order = generate_order()
    response = requests.post(url, data=json.dumps(order), headers=headers)
    print(f"Sent order: {order['orderId']} | Status: {response.status_code}")
    time.sleep(5)
