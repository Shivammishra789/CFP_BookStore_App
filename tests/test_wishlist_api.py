'''
@author: Shivam Mishra
@date: 02-02-22 12:56 AM
'''

import pytest
from main import app
from fastapi.testclient import TestClient
client = TestClient(app)


class TestWishlistApi:
    """
    Contains test cases for wishlist api
    """

    def test_for_data_in_wishlist_is_retrieved(self):
        response = client.get("/wishlist/", headers={
            "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MSwiZXhwaXJlcyI6MTY0MzcwMjg0OC4wOTM3Njg2fQ."
                     "P9NgeHvY06iM9Wo4TblBhkbBcMY5IWRSJr9eCwgALMk"})
        assert response.status_code == 200
        assert response.json()["message"] == "Successfully fetched wishlist"

    def test_if_wishlist_is_empty(self):
        response = client.get("/wishlist/", headers={
            "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9"
                     ".eyJ1c2VyX2lkIjpbeyJ1c2VyX2lkIjo0fV0sImV4cGlyZXMiOjE2NDM4MDQyNTQuNTM2NDUzfQ"
                     ".22pppG9o2J1nnvTmTGMKAwfjDWl323NdRAQ-gd0ia6g"})
        assert response.status_code == 200
        assert response.json()["message"] == "Error : Wishlist is empty"

    @pytest.mark.parametrize('wishlist_data', [
        {"book_id": 3}])
    def test_if_book_added_to_wishlist(self, wishlist_data):
        response = client.post("/wishlist/", headers={
            "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9"
                     ".eyJ1c2VyX2lkIjpbeyJ1c2VyX2lkIjo0fV0sImV4cGlyZXMiOjE2NDM4MDQyNTQuNTM2NDUzfQ"
                     ".22pppG9o2J1nnvTmTGMKAwfjDWl323NdRAQ-gd0ia6g"}, json=wishlist_data)
        assert response.json()["message"] == "Successfully Added Book to Wishlist"

    @pytest.mark.parametrize('wishlist_data', [
        {"book_id": 3}])
    def test_if_book_not_added_to_wishlist(self, wishlist_data):
        response = client.post("/wishlist/", headers={
            "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9"
                     ".eyJ1c2VyX2lkIjpbeyJ1c2VyX2lkIjo0fV0sImV4cGlyZXMiOjE2NDM4MDQyNTQuNTM2NDUzfQ"
                     ".22pppG9o2J1nnvTmTGMKAwfjDWl323NdRAQ-gd0ia6g"}, json=wishlist_data)
        assert response.json()["message"] == "Error : 1062 (23000): Duplicate entry '3' for key 'wishlist.book_id'"

    @pytest.mark.parametrize('wishlist_data', [
        {"book_id": 8}])
    def test_delete_from_wishlist(self, wishlist_data):
        response = client.delete("/wishlist/", headers={
        "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9"
                ".eyJ1c2VyX2lkIjpbeyJ1c2VyX2lkIjo0fV0sImV4cGlyZXMiOjE2NDM4MDQyNTQuNTM2NDUzfQ"
                ".22pppG9o2J1nnvTmTGMKAwfjDWl323NdRAQ-gd0ia6g"}, json = wishlist_data)
        assert response.json()["message"] == "Successfully Removed Book From Wishlist"

    @pytest.mark.parametrize('wishlist_data', [
        {"book_id": 8}])
    def test_for_book_id_already_deleted_wishlist(self, wishlist_data):
        response = client.delete("/wishlist/", headers={
            "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9"
                     ".eyJ1c2VyX2lkIjpbeyJ1c2VyX2lkIjo0fV0sImV4cGlyZXMiOjE2NDM4MDQyNTQuNTM2NDUzfQ"
                     ".22pppG9o2J1nnvTmTGMKAwfjDWl323NdRAQ-gd0ia6g"}, json=wishlist_data)
        assert response.json()["message"] == "Error : book id already deleted "