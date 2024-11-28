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



