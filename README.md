API Automation Testing Project

Automated API testing project built with Python, Pytest, and Requests.

Tools & Technologies:

- Python
- Pytest
- Requests
- Git & GitHub

Test Coverage:

- GET: Retrieve product data.
- POST: Create a new product.
- PUT: Update product data.
- PATCH: Update specific product fields.
- DELETE: Delete a product.
- Negative Testing: Validate invalid product data.

Negative Testing:

- Test product creation with a negative price.
- Test product creation without a title.

These two tests are marked as expected failures ("XFAIL") because DummyJSON accepts these inputs.

How to Run Tests

Install dependencies:

python -m pip install requests pytest

Run all tests:

python -m pytest -v

 Project Structure:
 
 - "api-automation-project/"
  - ".gitignore"
  - "README.md"
  - "test_get_products.py"
  - "test_products_operations.py"



API

"DummyJSON Products API" (https://dummyjson.com/products)
