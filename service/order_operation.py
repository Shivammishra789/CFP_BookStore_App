'''
@author: Shivam Mishra
@date: 30-01-22 12:16 AM
'''

from core.database_connection import DBConnection

connection = DBConnection().establish_connection()
cursor = connection.cursor(dictionary=True)


def place_new_order(address, user_id):
    """
        desc: place order
        param:  address, book_id
        :return: order_id
    """
    query = f"CALL sp_order(%d,'%s')" % (user_id, address)
    cursor.execute(query)
    connection.commit()
