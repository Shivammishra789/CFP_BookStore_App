'''
@author: Shivam Mishra
@date: 20-01-22 11:59 AM
@desc: Contains all api
'''

import logging
from fastapi import FastAPI, Header
from jwt_handler.jwt_handler import JwtHandler
from model.books_model import Book
from model.user_model import UserDetails
from send_email import send_email_async, send_email_background
from service.books_operation import BooksOperation
from service.user_operation import UserOperation

logging.basicConfig(filename='book_store.log', filemode='a', level=logging.DEBUG,
                    format='%(levelname)s :: %(name)s :: %(asctime)s :: %(message)s')

app = FastAPI()
operation = UserOperation()
operation = BooksOperation()



@app.get("/users", tags=["USERS"])
def retrieve_all_user_details():
    """
        desc: get method to retrieve all user details
        return: user details in SMD format
    """
    try:
        user_details = operation.get_all_user_details()
        logging.info("Successfully Fetched All User Details")
        logging.debug(f"Employee Details are : {user_details}")
        return {"status": 200, "message": "Employee Details fetched successfully", "data": user_details}
    except Exception as error:
        logging.error(f"Error: {error}")
        return {"status": 500, "message": f"Error : {error}"}


@app.get("/users", tags=["USERS"])
def single_user_data(user_id):
    """
        desc: get method to retrieve single user detail
        return: user detail in SMD format
    """
    try:
        user_detail = operation.get_single_user_detail(user_id)
        logging.info("Successfully Fetched User Details")
        logging.debug(f"User Details are : {user_detail}")
        return {"status": 200, "message": "Employee Details fetched successfully", "data": user_detail}
    except Exception as error:
        logging.error(f"Error: {error}")
        return {"status": 500, "message": f"{error}"}


@app.post("/users/register", tags=["USERS"])
async def register_user(user: UserDetails):
    """
        desc: post method to add user details
        param: email id, password, full name, mobile no
        return: token details in SMD format
    """
    try:
        user_id = operation.add_user(user.email_id, user.password, user.full_name, user.mobile_no)
        logging.info("Successfully Added User Details")
        logging.debug(f"Added User Id is : {user_id}")
        token_id = JwtHandler.encode_token(user_id)
        await send_email_async('USER VERIFICATION', user.email_id, {'token':token_id})
        return {"status": 200, "message": "User Details added successfully", "token": token_id}
    except Exception as error:
        logging.error(f"Error: {error}")
        return {"status": 500, "message": f"Error : {error}"}


@app.post("/users/login", tags=["USERS"])
def verify_existing_user(email_id: str, password: str):
    """
        desc: post method to verify existing user
        param: email id, password
        return: token details in SMD format
    """
    try:
        user_id = operation.verify_existing_user(email_id, password)
        logging.info("Successfully Verified User Details")
        logging.debug(f"Verified User Id is : {user_id}")
        token_id = JwtHandler.encode_token(user_id)
        return {"status": 200, "message": "User Verified successfully", "token": token_id}
    except Exception as error:
        logging.error(f"Error: {error}")
        return {"status": 500, "message": f"Error : {error}"}


@app.delete("/users", tags=["USERS"])
def delete_user(id:int):
    """
        desc: delete method to delete user details
        param: id
        return: deleted user id in SMD format
    """
    try:
        deleted_id = operation.delete_user(id)
        logging.info("Successfully Deleted The User Details")
        logging.debug(f"Deleted Employee ID is : {deleted_id}")
        return {"status": 200, "message": "Successfully Deleted The User Details",
                "data": f"Deleted user Id is {deleted_id}"}
    except Exception as error:
        logging.error(f"Error: {error}")
        return {"status": 500, "message": f"Error : {error}"}


@app.put("/users", tags=["USERS"])
def update_user_detail(id: int, update_param: str, update: str):
    """
        desc: put method to update user detail
        param: id, parameter to be updated
        return: updated user details in SMD format
    """
    try:
        updated_details = operation.update_user_detail(id, update_param, update)
        return {"status": 200, "message": "User Detail updated successfully", "data": updated_details}
    except Exception as error:
        logging.error(f"Error: {error}")
        return {"status": 500, "message": f"Error : {error}"}


@app.get("/books/all_books", tags=["BOOKS"])
def get_all_books_data():
    """
    desc: created an api to retrieve all the data in the book table
    return: book details
    """
    try:
        result = operation.show_all_books()
        logging.info("Successfully retrieved all books Details ")
        return {"status": 200, "message": "Successfully retrieved  all books Details", "data": result}
    except Exception as error:
        logging.error(f"error caught :{error}")
        return {"status": 500, "message": f"Error : {error}"}


@app.get("/books/", tags=["BOOKS"])
def get_book_by_id(book_id: int):
    """
    desc: created an api to retrieve all the data of about a book
    param: book_id which is unique for each book
    return: book details in SMD format
    """
    try:
        result = operation.show_book_data(book_id)
        logging.info("Successfully retrieved  book Details")
        return {"status": 200, "message": "Successfully retrieved  book Details", "data": result}
    except Exception as error:
        logging.error(f"error caught :{error}")
        return {"status": 500, "message": f"Error : {error}"}


@app.post("/books/add_book", tags=["BOOKS"])
def add_book(book: Book):
    """
    desc: created api to add one book to the database
    param: Book class which have all the attributes related to book
    return: book inserted details
    """
    try:
        result = operation.add_book_to_db(book.id, book.author, book.title, book.image, book.quantity, book.price,book.description)
        logging.info("Successfully added one book Details")
        return {"status": 200, "message": "Successfully added The book Details","data": result}
    except Exception as error:
        logging.error(f"error caught :{error}")
        return {"status": 500, "message": f"Error : {error}"}


@app.put("/book/update_book/", tags=["BOOKS"])
def update_book(book_id: int, book: Book):
    """
    desc: created api to update id, author, title, image, quantity, price, description of book to the database
    param: book id and book model
    return: updated book details in SMD format
    """
    try:
        result = operation.update_book(book_id, book.id, book.author, book.title, book.image, book.quantity, book.price,
                                      book.description)
        logging.info(f"updated the details with book id {book_id} ")
        return {"status": 200, "message": "Successfully updated the book Details", "data ": result}
    except Exception as error:
        logging.error(f"error caught :{error}")
        return {"status": 500, "message": f"Error : {error}"}


@app.delete("/book/delete/", tags=["BOOKS"])
def delete_book_by_id(book_id: int):
    """
    desc: created api to delete one book from the database
    param: book_id as path parameter
    return: deleted book details or error
    """
    try:
        operation.delete_book(book_id)
        logging.info(f"deleted book by using book_id {book_id}")
        return {"status": 200, "message": "Successfully deleted one book Details",
                "data": f"deleted book id = {book_id}"}
    except Exception as error:
        logging.error(f"error caught :{error}")
        return {"status": 500, "message": f"Error : {error}"}