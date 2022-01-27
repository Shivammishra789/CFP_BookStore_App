'''
@author: Shivam Mishra
@date: 20-01-22 11:59 AM
@desc: Contains all user api
'''

from logger.logger import logging
from fastapi import APIRouter, Header
from jwt_handler.jwt_handler import JwtHandler
from model.model import UserDetails
from service.send_email import send_email_async
from service.user_operation import UserOperation

route = APIRouter(prefix="/users", tags=["USERS"])
operation = UserOperation()


@route.get("/all_user_details")
def retrieve_all_user_details():
    """
        desc: get method to retrieve all user details
        return: user details in SMD format
    """
    try:
        user_details = operation.get_all_user_details()
        logging.info("Successfully Fetched All User Details")
        logging.debug(f"User Details are : {user_details}")
        return {"status": 200, "message": "User Details fetched successfully", "data": user_details}
    except Exception as error:
        logging.error(f"Error: {error}")
        return {"status": 500, "message": f"Error : {error}"}


@route.get("/")
def single_user_data(user_id):
    """
        desc: get method to retrieve single user detail
        return: user detail in SMD format
    """
    try:
        user_detail = operation.get_single_user_detail(user_id)
        logging.info("Successfully Fetched User Details")
        logging.debug(f"User Details are : {user_detail}")
        return {"status": 200, "message": "User Details fetched successfully", "data": user_detail}
    except Exception as error:
        logging.error(f"Error: {error}")
        return {"status": 500, "message": f"{error}"}


@route.post("/register")
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
        await send_email_async('USER VERIFICATION', user.email_id, token_id)
        return {"status": 200, "message": "User Details added successfully", "token": token_id}
    except Exception as error:
        logging.error(f"Error: {error}")
        return {"status": 500, "message": f"Error : {error}"}


@route.get("/verification")
def verify_registered_user(token_id: str):
    """
    desc: method to verify registered user
    :param token_id: generated while registering user
    :return: verified user id in SMD format
    """
    try:
        user_id = JwtHandler.decode_token(token_id)
        operation.verify_new_user(user_id)
        logging.info("Successfully Verified Registered User")
        logging.debug(f"Verified User Id is : {user_id}")
        return {"status": 200, "message": f"User Verified successfully"}
    except Exception as error:
        logging.error(f"Error: {error}")
        return {"status": 500, "message": f"Error : {error}"}


@route.post("/login")
def existing_user_login(email_id: str, password: str):
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


@route.delete("/")
def delete_user(id:int):
    """
        desc: delete method to delete user details
        param: id
        return: deleted user id in SMD format
    """
    try:
        operation.delete_user(id)
        logging.info("Successfully Deleted The User Details")
        logging.debug(f"Deleted Employee ID is : {id}")
        return {"status": 200, "message": "Successfully Deleted The User Details",
                "data": f"Deleted user Id is {id}"}
    except Exception as error:
        logging.error(f"Error: {error}")
        return {"status": 500, "message": f"Error : {error}"}


@route.put("/")
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


