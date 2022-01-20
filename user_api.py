'''
@author: Shivam Mishra
@date: 20-01-22 11:59 AM
@desc: Contains all user api
'''

import logging
from fastapi import FastAPI, Header
from jwt_handler import JwtHandler
from user_model import UserDetails
from user_operation import UserOperation

logging.basicConfig(filename='book_store.log', filemode='a', level=logging.DEBUG,
                    format='%(levelname)s :: %(name)s :: %(asctime)s :: %(message)s')

app = FastAPI()
operation = UserOperation()


@app.get("/user")
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
    except Exception as e:
        logging.error(f"Error: {e}")
        return {"status": 500, "message": f"Error : {e}"}


@app.get("/user")
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
    except Exception as e:
        logging.error(f"Error: {e}")
        return {"status": 500, "message": f"{e}"}


@app.post("/users/register")
def register_user(user: UserDetails):
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
        return {"status": 200, "message": "User Details added successfully", "token": token_id}
    except Exception as e:
        logging.error(f"Error: {e}")
        return {"status": 500, "message": f"Error : {e}"}


@app.post("/user/login")
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
    except Exception as e:
        logging.error(f"Error: {e}")
        return {"status": 500, "message": f"Error : {e}"}


@app.delete("/user")
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
    except Exception as e:
        logging.error(f"Error: {e}")
        return {"status": 500, "message": f"Error : {e}"}


@app.put("/user")
def update_user_detail(id: int, update_param: str, update: str):
    """
        desc: put method to update user detail
        param: id, parameter to be updated
        return: updated user details in SMD format
    """
    try:
        updated_details = operation.update_user_detail(id, update_param, update)
        return {"status": 200, "message": "User Detail updated successfully", "data": updated_details}
    except Exception as e:
        return {"status": 500, "message": f"Error : {e}"}


# @app.post("/login/")
# def login(token: str = Header(None)):
#     """
#         desc: employee login by entering the token number generated at employee creation time
#         param: token: encoded user id
#         return: user details in SMD format
#     """
#     try:
#         token_id = JwtHandler.decode_token(token)
#         check_emp_in_db = operation.get_single_emp_data(token_id)
#         return {"status": 200, "message": "Successfully Logged In", "data": check_emp_in_db}
#     except Exception as e:
#         logging.error(f"Error: {e}")
#         return {"status": 500, "message": "You are not authorized employee"}