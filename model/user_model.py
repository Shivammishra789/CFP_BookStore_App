'''
@author: Shivam Mishra
@date: 20-01-22 11:51 AM
@desc: contains schema for user details
'''

from pydantic import BaseModel


class UserDetails(BaseModel):
    """
    Contains different parameters of user like email, password, fullname
    """
    email_id: str
    password: str
    full_name: str
    mobile_no: str
