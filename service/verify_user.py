'''
@author: Shivam Mishra
@date: 25-01-22 12:03 PM
'''

from jwt_handler.jwt_handler import JwtHandler
from fastapi import Header, HTTPException


def verify_token(token: str = Header(None)):
    if token is None:
        raise HTTPException(status_code=401, detail="Token not provided in header")
    try:
        user_id = JwtHandler.decode_token(token)
        return user_id
    except Exception as exception:
        raise HTTPException(status_code=403, detail="Decoding error")


