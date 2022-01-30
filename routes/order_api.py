'''
@author: Shivam Mishra
@date: 27-01-22 11:58 PM
'''

from fastapi import APIRouter, Header, Depends
from logger.logger import logging
from service.order_operation import *
from service.verify_user import verify_token
from model.model import Order

route = APIRouter(prefix="/order", tags=["ORDER"])


@route.post("/")
def place_order(obj: Order, user_id=Depends(verify_token)):
    """
    desc: api to place order
    :param obj: Order class instance
    :param user_id: decoded user id after verification
    :return: order placed message in SMD format
    """
    try:
        result = place_new_order(obj.address, user_id)
        logging.info("Order placed successfully")
        logging.debug(f"Order placed for User id  is : {user_id}")
        return {"status": 200, "message": "Order placed successfully", "result": result}
    except Exception as error:
        logging.error(f"Error: {error}")
        return {"status": 404, "message": f"Error : {error}"}

