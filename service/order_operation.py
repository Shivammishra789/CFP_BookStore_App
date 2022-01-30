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
        :return: result_args
    """
    args = [user_id, f'{address}']
    result_args = cursor.callproc('sp_order', args)
    connection.commit()
    return result_args
