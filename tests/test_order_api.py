'''
@author: Shivam Mishra
@date: 02-02-22 6:44 AM
'''

import pytest
from main import app
from fastapi.testclient import TestClient
client = TestClient(app)


class TestOrderApi:
    """
    Contains test cases for order api
    """

    @pytest.mark.parametrize('order_data', [
        {"address": 'Pune'}])
    def test_if_order_is_placed(self, order_data):
        response = client.post("/order/", headers={
            "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9"
                     ".eyJ1c2VyX2lkIjpbeyJ1c2VyX2lkIjo0fV0sImV4cGlyZXMiOjE2NDM4MjI0OTYuNTEwMDQ3NH0"
                     ".BKcIb992tK6imZWW1cRRa2l-X7fQeGMUkVCQj7d3KVc"}, json=order_data)
        assert response.json()["message"] == "Order placed successfully"

    @pytest.mark.parametrize('order_data', [
        {"address": 'Pune'}])
    def test_for_wrong_token_order_is_not_placed(self, order_data):
        response = client.post("/order/", headers={
            "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9"
                     ".yJ1c2VyX2lkIjpbeyJ1c2VyX2lkIjo0fV0sImV4cGlyZXMiOjE2NDM4MjI0OTYuNTEwMDQ3NH0"
                     ".BKcIb992tK6imZWW1cRRa2l-X7fQeGMUkVCQj7d3KVc"}, json=order_data)
        assert response.json()["detail"] == "Decoding error"