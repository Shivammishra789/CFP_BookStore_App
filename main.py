'''
@author: Shivam Mishra
@date: 24-01-22 11:40 AM
'''

from fastapi import FastAPI
from routes import user_api
from routes import book_api
from routes import wishlist_api
from routes import cart_api
from routes import order_api


app = FastAPI(title="Book Store App")

app.include_router(user_api.route)
app.include_router(book_api.route)
app.include_router(wishlist_api.route)
app.include_router(cart_api.route)
app.include_router(order_api.route)

