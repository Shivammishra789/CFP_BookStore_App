'''
@author: Shivam Mishra
@date: 25-01-22 10:26 PM
'''

from fastapi import APIRouter, Header, Depends
from logger.logger import logging
from service.wishlist_operation import show_wishlist, add_book_to_wishlist, delete_book_from_wishlist
from service.verify_user import verify_token
from model.model import Wishlist

route = APIRouter(prefix="/wishlist", tags=["WISHLIST"])


@route.get("/")
def view_wishlist(user_id=Depends(verify_token)):
    """
    desc: api to view all books in wishlist
    :param user_id: decoded user id after verification
    :return: wishlist in SMD format
    """
    try:
        wish_list = show_wishlist(user_id)
        logging.info("Successfully Get All Books From Wishlist")
        logging.debug(f"User Wishlist details are : {wish_list}")
        return {"status": 200, "message": "Successfully Got  Wishlist", "data": wish_list}
    except Exception as error:
        logging.error(f"Error: {error}")
        return {"status": 404, "message": f"Error : {error}"}


@route.post("/")
def add_to_wishlist(obj: Wishlist, user_id=Depends(verify_token)):
    """
    desc: api to add book to wishlist
    :param obj: instance of wishlist class
    :param user_id: decoded user id after verification
    :return: added book id in SMD format
    """
    try:
        added_book_id = add_book_to_wishlist(obj.book_id,user_id)
        logging.info("Successfully Added Book to Wishlist")
        logging.debug(f"Added book id  is : {added_book_id}")
        return {"status": 200, "message": "Successfully Added Book to Wishlist", "book_id": added_book_id}
    except Exception as error:
        logging.error(f"Error: {error}")
        return {"status": 404, "message": f"Error : {error}"}


@route.delete("/")
def remove_from_wishlist(obj:Wishlist,user_id=Depends(verify_token)):
    """
    desc: api to remove book from wishlist
    :param obj: instance of wishlist class
    :param user_id: decoded user id after verification
    :return: deleted book id in SMD format
    """
    try:
        removed_book_id = delete_book_from_wishlist(obj.book_id,user_id)
        logging.info("Successfully Removed Book From Wishlist")
        logging.debug(f"Removed book id  is : {removed_book_id}")
        return {"status": 200, "message": "Successfully Removed Book From Wishlist", "book_id": removed_book_id}
    except Exception as error:
        logging.error(f"Error: {error}")
        return {"status": 404, "message": f"Error : {error}"}