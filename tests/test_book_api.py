'''
@author: Shivam Mishra
@date: 01-02-22 03:24 PM
'''

import pytest
from main import app
from fastapi.testclient import TestClient
client = TestClient(app)


class TestBookApi:
    """
    Contains test cases for books api
    """

    def test_for_all_book_details_are_retrieved(self):
        response = client.get("/books/details/all")
        assert response.status_code == 200
        assert response.json()["message"] == "Successfully retrieved  all books Details"

    @pytest.mark.parametrize('book_id', [40])
    def test_to_retrieve_one_book_data(self, book_id):
        response = client.get(f"/books/details/book_id={book_id}")
        assert response.status_code == 200
        assert response.json()["message"] == "Successfully retrieved  book Details"

    @pytest.mark.parametrize('book_id', [56])
    def test_to_retrive_book_data_for_wrong_book_id(self, book_id):
        response = client.get(f"/books/details/book_id={book_id}")
        assert response.status_code == 200
        assert response.json()[0]['detail'] == "this book id is not present in the database"

    @pytest.mark.parametrize('book_data', [
        {"id": 101, "author": "manva", "title": "the dark knight", "image": "abc.jpg",
         "quantity": 15, "price": 350, "description": "bright"}])
    def test_to_add_book_to_db(self, book_data):
        response = client.post("/books/", json=book_data)
        assert response.json()["message"] == "Successfully added The book Details"

    @pytest.mark.parametrize('book_data', [
        {"id": 101, "author": "manva", "title": "the dark knight", "image": "abc.jpg",
         "quantity": 15, "price": 350, "description": "bright"}])
    def test_same_book_id_does_not_get_added_to_db(self, book_data):
        response = client.post("/books/", json=book_data)
        assert response.json()["message"] == "Error : 1062 (23000): Duplicate entry '101' for key 'books.PRIMARY'"

    @pytest.mark.parametrize('book_id,book_data', [(101,
        {"id": 101, "author": "manav", "title": "the dark knight", "image": "abc.jpg",
         "quantity": 15, "price": 3500, "description": "bright"})])
    def test_to_update_book_to_db(self, book_id, book_data):
        response = client.put(f"/books/?book_id={book_id}", json=book_data)
        assert response.status_code == 200
        assert response.json()["message"] == "Successfully updated the book Details"

    @pytest.mark.parametrize('book_id,book_data', [(301,
        {"id": 101, "author": "manav", "title": "the dark knight", "image": "abc.jpg",
         "quantity": 15, "price": 3500, "description": "bright"})])
    def test_wrong_book_id_cannot_be_updated(self, book_id, book_data):
        response = client.put(f"/books/?book_id={book_id}", json=book_data)
        assert response.status_code == 200
        assert response.json()["message"] != "Successfully updated the book Details"

    @pytest.mark.parametrize('book_id', [52])
    def test_for_book_gets_deleted_from_database(self, book_id):
        response = client.delete(f"/books/?book_id={book_id}")
        assert response.status_code == 200
        assert response.json()["message"] == "Successfully deleted one book Details"

    @pytest.mark.parametrize('book_id', [500])
    def test_delete_for_wrong_book_id(self, book_id):
        response = client.delete(f"/books/?book_id={book_id}")
        assert response.status_code == 200
        assert response.json()["message"] == "Error : Entered book id not found"
