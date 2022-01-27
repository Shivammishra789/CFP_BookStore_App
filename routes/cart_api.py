'''
@author: Shivam Mishra
@date: 27-01-22 6:06 PM
'''

from fastapi import APIRouter, Header, Depends
from logger.logger import logging
from service.cart_operation import *
from service.verify_user import verify_token
from model.model import Cart

route = APIRouter(prefix="/cart", tags=["CART"])


@route.get("/")
def view_cart(user_id=Depends(verify_token)):
    """
    desc: api to view all books in cart
    :param user_id: decoded user id after verification
    :return: cart in SMD format
    """
    try:
        cart_details = show_cart(user_id)
        logging.info("Successfully Get All Books From cart")
        logging.debug(f"User Cart details are : {cart_details}")
        return {"status": 200, "message": "Cart Details Fetched Successfully", "data": cart_details}
    except Exception as error:
        logging.error(f"Error: {error}")
        return {"status": 404, "message": f"Error : {error}"}


@route.post("/")
def add_to_cart(obj: Cart, user_id=Depends(verify_token)):
    """
    desc: api to add book to cart
    :param obj: instance of cart class
    :param user_id: decoded user id after verification
    :return: added book id in SMD format
    """
    try:
        added_book_id = add_book_to_cart(obj.book_id,user_id)
        logging.info("Successfully Added Book to Cart")
        logging.debug(f"Added book id  is : {added_book_id}")
        return {"status": 200, "message": "Successfully Added Book to Cart", "book_id": added_book_id}
    except Exception as error:
        logging.error(f"Error: {error}")
        return {"status": 404, "message": f"Error : {error}"}


@route.delete("/")
def remove_from_cart(book_id: int, user_id=Depends(verify_token)):
    """
    desc: api to remove book from cart
    :param book_id: book id to be deleted
    :param user_id: decoded user id after verification
    :return: deleted book id in SMD format
    """
    try:
        removed_book_id = delete_book_from_cart(book_id,user_id)
        logging.info("Successfully Removed Book From Cart")
        logging.debug(f"Removed book id  is : {removed_book_id}")
        return {"status": 200, "message": "Successfully Removed Book From Cart", "book_id": removed_book_id}
    except Exception as error:
        logging.error(f"Error: {error}")
        return {"status": 404, "message": f"Error : {error}"}


@route.put("/")
def update_quantity(book_id: int, quantity: int, user_id=Depends(verify_token)):
    """
    desc: api to update book quantity in cart
    :param quantity: quantity
    :param book_id: book id whose quantity will be updated
    :param user_id: decoded user id after verification
    :return: book id with updated quantity of books in SMD format
    """
    try:
        updated_quantity = update_quantity_of_book_in_cart(book_id, user_id, quantity)
        logging.info("Successfully Updated Book Quantity In Cart")
        logging.debug(f"Updated book quantity for user id: {user_id} is {updated_quantity}")
        return {"status": 200, "message": "Successfully Updated Book Quantity In Cart",
                "updated quantity": updated_quantity, "for user id": user_id}
    except Exception as error:
        logging.error(f"Error: {error}")
        return {"status": 404, "message": f"Error : {error}"}