'''
@author: Shivam Mishra
@date: 25-01-22 10:35 PM
'''
from core.database_connection import DBConnection

connection = DBConnection().establish_connection()
cursor = connection.cursor(dictionary=True)


def show_wishlist(user_id):
    """
        desc: displaying wishlist details from database
        param: user_id
        return: wish_list in dict format
    """

    query = '''SELECT books.author, books.title, books.price, books.image from books
               join wishlist on wishlist.book_id = books.id where user_id = %d''' % user_id
    cursor.execute(query)
    wish_list = [i for i in cursor]
    if wish_list:
        return wish_list
    else:
        raise Exception("There is no result for the Wishlist.")


def add_book_to_wishlist(book_id,user_id):
    """
        desc: adding book to wishlist
        param:  user_id, book_id
    """
    query = f"INSERT INTO wishlist (user_id,book_id) values (%d,%d)" %(user_id,book_id)
    cursor.execute(query)
    connection.commit()
    return book_id


def delete_book_from_wishlist(book_id,user_id):
    """
        desc: deleting book from wishlist
        param:  user_id, book_id
    """
    query = f"DELETE FROM wishlist WHERE user_id = %d AND book_id = %d" %(user_id,book_id)
    cursor.execute(query)
    connection.commit()
    return book_id
