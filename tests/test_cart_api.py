'''
@author: Shivam Mishra
@date: 02-02-22 1:00 AM
'''

import pytest
from main import app
from fastapi.testclient import TestClient
client = TestClient(app)


class TestForCartApi:
    """
    Contains test cases for cart api
    """

    def test_for_data_in_cart_is_retrieved(self):
        response = client.get("/cart/", headers={
            "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9"
                     ".eyJ1c2VyX2lkIjpbeyJ1c2VyX2lkIjo0fV0sImV4cGlyZXMiOjE2NDM4MjI0OTYuNTEwMDQ3NH0"
                     ".BKcIb992tK6imZWW1cRRa2l-X7fQeGMUkVCQj7d3KVc"})
        assert response.status_code == 200
        assert response.json()["message"] == "Cart Details Fetched Successfully"

    def test_if_cart_is_empty(self):
        response = client.get("/cart/", headers={
             "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9"
                     ".eyJ1c2VyX2lkIjpbeyJ1c2VyX2lkIjo0fV0sImV4cGlyZXMiOjE2NDM4MjI0OTYuNTEwMDQ3NH0"
                     ".BKcIb992tK6imZWW1cRRa2l-X7fQeGMUkVCQj7d3KVc"})
        assert response.status_code == 200
        assert response.json()["data"] == "Cart is empty"

    @pytest.mark.parametrize('cart_data', [
        {"book_id": 4}])
    def test_if_book_added_to_cart(self, cart_data):
        response = client.post("/cart/", headers={
             "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9"
                     ".eyJ1c2VyX2lkIjpbeyJ1c2VyX2lkIjo0fV0sImV4cGlyZXMiOjE2NDM4MjI0OTYuNTEwMDQ3NH0"
                     ".BKcIb992tK6imZWW1cRRa2l-X7fQeGMUkVCQj7d3KVc"}, json=cart_data)
        assert response.json()["message"] == "Successfully Added Book to Cart"

    @pytest.mark.parametrize('book_id,quantity', [
        (4, 5)])
    def test_for_update_quantity_into_cart(self, book_id, quantity):
        response = client.put(f"/cart/?book_id={book_id}&quantity={quantity}", headers={
            "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9"
                     ".eyJ1c2VyX2lkIjpbeyJ1c2VyX2lkIjo0fV0sImV4cGlyZXMiOjE2NDM4MjI0OTYuNTEwMDQ3NH0"
                     ".BKcIb992tK6imZWW1cRRa2l-X7fQeGMUkVCQj7d3KVc"})
        assert response.status_code == 200
        assert response.json()["message"] == "Successfully Updated Book Quantity In Cart"

    @pytest.mark.parametrize('book_id,quantity', [
        (52, 5)])
    def test_for_book_id_not_in_db_update_quantity_into_cart(self, book_id, quantity):
        response = client.put(f"/cart/?book_id={book_id}&quantity={quantity}", headers={
            "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9"
                     ".eyJ1c2VyX2lkIjpbeyJ1c2VyX2lkIjo0fV0sImV4cGlyZXMiOjE2NDM4MjI0OTYuNTEwMDQ3NH0"
                     ".BKcIb992tK6imZWW1cRRa2l-X7fQeGMUkVCQj7d3KVc"})
        assert response.status_code == 200
        assert response.json()["message"] == "Error : id not found"

    @pytest.mark.parametrize('cart_data', [
        {"book_id": 4}])
    def test_delete_from_cart(self, cart_data):
        response = client.delete("/cart/", headers={
            "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9"
                     ".eyJ1c2VyX2lkIjpbeyJ1c2VyX2lkIjo0fV0sImV4cGlyZXMiOjE2NDM4MjI0OTYuNTEwMDQ3NH0"
                     ".BKcIb992tK6imZWW1cRRa2l-X7fQeGMUkVCQj7d3KVc"}, json=cart_data)
        assert response.json()["message"] == "Successfully Removed Book From Cart"

    @pytest.mark.parametrize('cart_data', [
        {"book_id": 8}])
    def test_for_book_id_already_deleted_cart(self, cart_data):
        response = client.delete("/wishlist/", headers={
             "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9"
                     ".eyJ1c2VyX2lkIjpbeyJ1c2VyX2lkIjo0fV0sImV4cGlyZXMiOjE2NDM4MjI0OTYuNTEwMDQ3NH0"
                     ".BKcIb992tK6imZWW1cRRa2l-X7fQeGMUkVCQj7d3KVc"}, json=cart_data)
        assert response.json()["message"] == "Error : book id already deleted "
