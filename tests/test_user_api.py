'''
@author: Shivam Mishra
@date: 31-01-22 03:44 PM
'''


import pytest
from main import app
from fastapi.testclient import TestClient
client = TestClient(app)


class TestForUserApi:
    """
    Contains test cases for user api
    """

    def test_all_user_details_are_retrieved(self):
        response = client.get("/users/details/all")
        assert response.status_code == 200
        assert response.json()["message"] == "User Details fetched successfully"

    @pytest.mark.parametrize('user_id', [4])
    def test_single_user_details_is_retrieved(self, user_id):
        response = client.get(f"/users/details/user_id={user_id}")
        assert response.status_code == 200
        assert response.json()["message"] == "User Details fetched successfully"

    @pytest.mark.parametrize('user_id', [12])
    def test_for_user_details_is_not_present(self, user_id):
        response = client.get(f"/users/details/user_id={user_id}")
        assert response.status_code == 200
        assert response.json()["message"] == "('User Details cannot be fetched', 'error: id not found')"

    @pytest.mark.parametrize('user_data', [
        { 'email_id': 'shivammishra7789@gmail.com','password': '123', 'full_name': 'Shivam', 'mobile_no': '9874589765'}])
    def test_for_adding_user_to_db(self, user_data):
        response = client.post("/users/register", json=user_data)
        assert response.status_code == 200
        assert response.json()["message"] == "User Details added successfully"

    @pytest.mark.parametrize('user_data', [
        { 'email_id': 'shivam@gmail.com','password': '123', 'full_name': 'Mahi', 'mobile_no': '9874589765'}])
    def test_for_same_user_does_not_get_added(self, user_data):
        response = client.post("/users/register", json=user_data)
        assert response.status_code == 404
        assert response.json()["message"] == "Error : 1062 (23000): Duplicate entry 'shivam@gmail.com' for key " \
                                             "'user_details.unique_email'"

    @pytest.mark.parametrize('user_data', [
        { 'email_id': 'shivam@gmail.com','password': '123', 'full_name': 'Mahi', 'mobile_no': '9874589765'}])
    def test_for_user_does_not_get_added_to_db(self, user_data):
        response = client.post("/users/register", json=user_data)
        assert response.status_code == 200
        assert response.json()["message"] != "User Details added successfully"

    @pytest.mark.parametrize('token',["eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9"
                                      ".eyJ1c2VyX2lkIjpbeyJ1c2VyX2lkIjo0fV0sImV4cGlyZXMiOjE2NDM3ODc0NTguODA3MDgzOH0"
                                      ".y-4yZDBvQ6T7-adpgAgOkV8tZiMdks-CcV5aIm9vCxo"])
    def test_for_registered_user_verification_is_successful(self, token):
        response = client.get(f"/users/verification?token_id={token}")
        assert response.status_code == 200
        assert response.json()['message'] == "User Verified successfully"

    @pytest.mark.parametrize('token', ["eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9"
                                       ".1c2VyX2lkIjpbeyJ1c2VyX2lkIjoyfV0sImV4cGlyZXMiOjE2NDM3ODY4MjguNjk3NzU0OX0"
                                       ".vs3sFW9itXUi6oxlFLd_wKwLSS1zOSHuH5HrMD5Dv1Q"])
    def test_for_registered_user_verification_is_not_successful(self, token):
        response = client.get(f"/users/verification?token_id={token}")
        assert response.status_code == 200
        assert response.json()['message'] == "Error : Signature verification failed"

    @pytest.mark.parametrize('id, update_param, update', [
        (3, 'full_name','Shiv')])
    def test_for_user_details_are_updated_to_db(self, id, update_param, update):
        response = client.put(f"/users/?id=3&update_param={update_param}&update={update}")
        assert response.status_code == 200
        assert response.json()["message"] == "User Detail updated successfully"

    @pytest.mark.parametrize('id, update_param, update', [
        (66, 'full_name','Shiv')])
    def test_for_user_details_not_updated_to_db(self, id, update_param, update):
        response = client.put(f"/users/?id=3&update_param={update_param}&update={update}")
        assert response.status_code == 200
        assert response.json()["message"] == "Error : ('User Details cannot be fetched', 'error: id not found')"

    @pytest.mark.parametrize('user_id', [5])
    def test_for_user_details_is_deleted_from_database(self, user_id):
        response = client.delete(f"/users/delete_user/user_id={user_id}")
        assert response.status_code == 200
        assert response.json()["message"] == "Successfully Deleted The User Details"

    @pytest.mark.parametrize('user_id', [(122)])
    def test_for_user_details_is_not_deleted_from_database(self, user_id):
        response = client.delete(f"/users/delete_user/user_id={user_id}")
        assert response.status_code == 200
        assert response.json()["message"] == "Error : id not found"

    @pytest.mark.parametrize('email_id , password', [('shivammishra7789@gmail.com', '123')])
    def test_if_login_is_successful(self, email_id, password):
        response = client.post(f"/users/login/?email_id={email_id}&password={password}")
        assert response.json()['message'] == "User Verified successfully"

    @pytest.mark.parametrize('email_id , password', [('shivammishra7789@gmail.com', 'd223@3')])
    def test_if_login_is_not_successful(self, email_id, password):
        response = client.post(f"/users/login/?email_id={email_id}&password={password}")
        assert response.json()['message'] == "Error : ('Incorrect User Details', 'error: id not found')"

