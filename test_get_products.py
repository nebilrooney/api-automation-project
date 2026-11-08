import requests

def test_get_product():
    response = requests.get(
        "https://dummyjson.com/product/1"
    )

    data = response.json()

    assert response.status_code == 200
    assert data["id"] == 1
    assert isinstance(data["price"], (int, float))
    assert "brand" in data
    assert data["brand"] != ""


def test_multiple_products():
    response = requests.get(
        "https://dummyjson.com/products?limit=3"
    )

    data = response.json()
    products = data["products"]

    assert len(products) == 3

    for product in products:
        assert product["id"] > 0
        assert product["price"] > 0


def test_product_not_found():
    response = requests.get(
        "https://dummyjson.com/product/999999"
    ) 

    assert response.status_code == 404

    data = response.json()
    assert "not found" in data["message"]     
