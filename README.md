Receipt Processor API

A simple Flask-based API for processing receipts and calculating loyalty points based on certain rules. The API is designed to process receipt information in a structured format, store the points associated with the receipt, and allow retrieval of points based on a receipt ID.

Design Decisions

1. Flask Web Framework 
Flask is used to create the API because of its simplicity, flexibility, and lightweight nature. It provides all the necessary components for quickly building a RESTful API.
Flask's built-in development server is used, though a production-grade WSGI server (like Gunicorn) would be recommended for deployment.

2. Data Storage
The receipt data and associated points are stored in memory (using a Python dictionary) for simplicity. This is not a production-level database, but serves the purpose for testing and quick iterations.
The store_receipt and get_points_by_id functions handle the storing and retrieving of receipt data.

3. Docker 
Docker is used to containerize the application for easier deployment and testing. The Dockerfile defines the environment, installs dependencies, and runs the Flask app.
Docker Compose is used to manage the application’s services, making it easier to spin up and manage containers locally.

4. Calculation of Points
The logic for calculating points is based on several rules defined in the logic.py file. These rules take into account the retailer, total amount, items purchased, and the time of the purchase, among other factors.
The point calculation system is modular, allowing for easy updates to the calculation rules in the future.

Setup Instructions 
Prerequisits: 
Docker
Docker Compose 

Steps to Run the Application 

1. Clone the repository
   git clone https://github.com/lovpret-kaur/receipt-processor.git

   cd receipt-processor
3. Build and start the application
   docker-compose up --build
4. Once the container is up and running, verify the API is working by navigating to http://localhost:8000. You should see "API is running"
5. API Endpoints
   1. POST /receipts/process
   This endpoint processes a receipt and returns a unique receipt ID.
   
   Request Body:

   {
  "retailer": "Target",
  "purchaseDate": "2022-01-01",
  "purchaseTime": "13:01",
  "items": [
    {"shortDescription": "Mountain Dew 12PK", "price": "6.49"},
    {"shortDescription": "Emils Cheese Pizza", "price": "12.25"},
    {"shortDescription": "Knorr Creamy Chicken", "price": "1.26"},
    {"shortDescription": "Doritos Nacho Cheese", "price": "3.35"},
    {"shortDescription": "Klarbrunn 12-PK 12 FL OZ", "price": "12.00"}
  ],
  "total": "35.35"
   }

   Response:

   {
  "id": "96a8c783-5c4b-4517-96f4-bc70d8bc9bd2"
   }

   2. GET /receipts/{receipt_id}/points
   This endpoint retrieves the points for a given receipt ID.
   
   curl http://localhost:8000/receipts/<id>/points

   Response:

   {
  "points": 109
   }





