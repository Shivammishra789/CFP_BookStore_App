'''
@author: Shivam Mishra
@date: 23-01-22 1:24 PM
@desc: contains all schema for book_store app
'''

from pydantic import BaseModel


class UserDetails(BaseModel):
    """
    Contains different parameters of user like email, password, fullname, mobile_no
    """
    email_id: str
    password: str
    full_name: str
    mobile_no: str


class Book(BaseModel):
    """
    this class contains attributes related to book details
    """
    id: int
    author: str
    title: str
    image: str
    quantity: int
    price: float
    description: str


class Wishlist(BaseModel):
    """
    Contains book_id
    """
    book_id: int


class Cart(BaseModel):
    """
    Contains book_id
    """
    book_id: int


