'''
@author: Shivam Mishra
@date: 23-01-22 1:24 PM
'''

from pydantic import BaseModel


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