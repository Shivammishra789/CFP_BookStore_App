'''
@author: Shivam Mishra
@date: 24-01-22 11:40 AM

'''

import user_api
import book_api
from fastapi import FastAPI

app = FastAPI(title="Book Store App")

app.include_router(user_api.route)
app.include_router(book_api.route)
