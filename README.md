# Serverless Order Tracker Using DynamoDB

This project is a real-time **serverless order tracking system** built using **AWS services** like DynamoDB, Lambda, API Gateway, S3, and SNS. It demonstrates how to collect, process, store, and notify order events in a scalable and event-driven architecture without managing any servers.

---

##  Tech Stack

- **AWS Lambda** – serverless functions to handle order events and stream processing  
- **Amazon API Gateway** – REST endpoint to receive new orders  
- **Amazon DynamoDB** – NoSQL database to store all orders  
- **DynamoDB Streams** – trigger Lambda on item insert  
- **Amazon S3** – save order JSON logs in real-time  
- **Amazon SNS** – send email notifications on new orders  
- **CloudWatch** – for logging and debugging Lambda execution  
- **GitHub** – for code versioning  
- **Python** – backend implementation

---

##  Features

- Create new orders using a REST API
- Store orders in DynamoDB with timestamp
- Stream changes (INSERT) using DynamoDB Streams
- Lambda triggered on every new order → saves `.json` log to S3
- Lambda also publishes a notification to SNS → sends email
- Fully serverless architecture – no EC2 or backend server needed
- Realtime order logging and alerting

---

