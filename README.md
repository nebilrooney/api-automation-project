API Automation Testing Project

Project Description

This project contains automated API tests using Python, Pytest, and Requests.

Tools & Technologies

- Python
- Pytest
- Requests
- Git & GitHub

Test Coverage

- GET: Retrieve product data.
- POST: Create a new product.
- PUT: Update product data.
- PATCH: Update specific product fields.
- DELETE: Delete a product.
- Negative Testing: Validate invalid product data.

How to Run Tests

Install dependencies:

python -m pip install requests pytest

Run all tests:

python -m pytest -v

Project Structure

api-automation-project/
├── .gitignore
├── README.md
├── test_get_products.py
└── test_products_operations.py

API

DummyJSON: https://dummyjson.com/products
