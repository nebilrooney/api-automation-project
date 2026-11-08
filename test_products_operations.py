import pytest
import requests


def test_create_product():
    response = requests.post(
        "https://dummyjson.com/product/add", json={"title": "Test Product", "price": 100}
    )

    data = response.json()  

    assert response.status_code == 201
    assert data["title"] == "Test Product" 
    assert data["price"] == 100
    assert isinstance(data["price"], (int, float))


@pytest.mark.xfail(reason="API accepts negative price")
def test_negative_product_price():
    response = requests.post(
        "https://dummyjson.com/products/add", json={"title": "Invalid Product", "price": -50}
    ) 

    data = response.json() 

    assert data["price"] >= 0

    print(response.status_code)  
    print(data)


@pytest.mark.xfail(reason="API accepts missing title")
def test_product_without_title():
    response = requests.post(
        "https://dummyjson.com/products/add", json={"price": 100}
    ) 

    data = response.json()

    assert response.status_code == 400

    print(response.status_code)
    print(data) 


def test_update_product():
    response = requests.put(
        "https://dummyjson.com/products/1", json={"title": "Updated Product"}
    )      

    data = response.json()

    assert response.status_code == 200
    assert data["title"] == "Updated Product"


def test_update_product_price():
    response = requests.patch(
        "https://dummyjson.com/products/1", json={"price": 600}
    )    

    data = response.json()

    assert response.status_code == 200
    assert data["price"] == 600

def test_delete_product():
    response = requests.delete(
        "https://dummyjson.com/products/1"
    )

    data = response.json()

    assert response.status_code == 200
    assert data["isDeleted"] == True   