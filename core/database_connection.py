'''
@author: Shivam Mishra
@date: 20-01-22 11:40 AM
@desc: establish connection with database
'''

import logging
from mysql.connector import connect, Error
import os
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(filename='book_store.log', filemode='a', level=logging.DEBUG,
                    format='%(levelname)s :: %(name)s :: %(asctime)s :: %(message)s')


class DBConnection:
    """
    Contains method to establish connection with database
    """

    @staticmethod
    def establish_connection():
        """
        desc: establish connection with database
        return: connection
        """
        try:
            logging.info("Trying to establish the database connection")
            connection = connect(
                host=os.getenv('host'),
                user=os.getenv('user_name'),
                password=os.getenv('password'),
                database='book_store'
            )
            logging.info("Database Connection is Established")
            return connection
        except Error:
            logging.error("Connection not Established")
            return {"status": 502, "message": "Error : Connection not Established"}

