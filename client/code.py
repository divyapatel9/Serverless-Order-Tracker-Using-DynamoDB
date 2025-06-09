import requests
import json

url = "https://o9oksk3qg7.execute-api.us-east-2.amazonaws.com/prod/order"

order = {
    "orderId": "order999", 
    "user": "divya@example.com",
    "product": "Tablet",
    "quantity": 3,
    "timestamp": "2025-06-09T18:30:00Z"
}


headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, data=json.dumps(order), headers=headers)

print("Status Code:", response.status_code)
print("Response:", response.text)
