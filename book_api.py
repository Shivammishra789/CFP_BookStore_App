'''
@author: Shivam Mishra
@date: 24-01-22 11:29 AM

'''
from logger import logging
from fastapi import APIRouter
from model.books_model import Book
from service.book_operation import BooksOperation

route = APIRouter(prefix="/books", tags=["BOOKS"])
book_operation = BooksOperation()


@route.get("/all_book_details")
def get_all_books_details():
    """
    desc: created an api to retrieve all the data in the book table
    return: book details
    """
    try:
        result = book_operation.show_all_books_data()
        logging.info("Successfully retrieved all books Details ")
        return {"status": 200, "message": "Successfully retrieved  all books Details", "data": result}
    except Exception as error:
        logging.error(f"Error :{error}")
        return {"status": 500, "message": f"Error : {error}"}


@route.get("/")
def get_book_details_by_id(book_id: int):
    """
    desc: created an api to retrieve all the data of about a book
    param: book_id which is unique for each book
    return: book details in SMD format
    """
    try:
        result = book_operation.show_single_book_data(book_id)
        logging.info("Successfully retrieved  book Details")
        return {"status": 200, "message": "Successfully retrieved  book Details", "data": result}
    except Exception as error:
        logging.error(f"Error :{error}")
        return {"status": 500, "message": f"Error : {error}"}


@route.post("/")
def add_book(book: Book):
    """
    desc: created api to add one book to the database
    param: Book class which have all the attributes related to book
    return: book inserted details
    """
    try:
        result = book_operation.add_single_book(book.id, book.author, book.title, book.image, book.quantity, book.price,book.description)
        logging.info("Successfully added one book Details")
        return {"status": 200, "message": "Successfully added The book Details","data": result}
    except Exception as error:
        logging.error(f"error caught :{error}")
        return {"status": 500, "message": f"Error : {error}"}


@route.put("/")
def update_book(book_id: int, book: Book):
    """
    desc: created api to update id, author, title, image, quantity, price, description of book to the database
    param: book id and book model
    return: updated book details in SMD format
    """
    try:
        result = book_operation.update_book(book_id, book.id, book.author, book.title, book.image,
                                            book.quantity, book.price,book.description)
        logging.info(f"updated the details with book id {book_id} ")
        return {"status": 200, "message": "Successfully updated the book Details", "data ": result}
    except Exception as error:
        logging.error(f"Error :{error}")
        return {"status": 500, "message": f"Error : {error}"}


@route.delete("/")
def delete_book_by_id(book_id: int):
    """
    desc: created api to delete one book from the database
    param: book_id as path parameter
    return: deleted book id in SMD format
    """
    try:
        book_operation.delete_book(book_id)
        logging.info(f"deleted book by with book_id {book_id}")
        return {"status": 200, "message": "Successfully deleted one book Details",
                "data": f"deleted book id = {book_id}"}
    except Exception as error:
        logging.error(f"Error :{error}")
        return {"status": 500, "message": f"Error : {error}"}