'''
@author: Shivam Mishra
@date: 27-01-22 8:16 PM
'''

from core.database_connection import DBConnection

connection = DBConnection().establish_connection()
cursor = connection.cursor(dictionary=True)


def show_cart(user_id):
    """
        desc: displaying cart details from database
        param: user_id
        return: cart in dict format
    """

    query = '''SELECT books.author, books.title, books.price, books.image, cart.quantity  from books
               join cart on cart.book_id = books.id where user_id = %d''' % user_id
    cursor.execute(query)

    cart = [i for i in cursor]
    if cart:
        connection.commit()
        return cart
    else:
        msg = "Cart is empty"
        return msg


def add_book_to_cart(book_id,user_id):
    """
        desc: adding book to cart
        param:  user_id, book_id
        :return: book_id
    """
    query = f"INSERT INTO cart (user_id,book_id) values (%d,%d)" %(user_id,book_id)
    cursor.execute(query)
    connection.commit()
    return book_id


def delete_book_from_cart(book_id,user_id):
    """
        desc: deleting book from cart
        param:  user_id, book_id
        :return: book_id
    """
    cursor.execute(f'select user_id from cart where user_id={user_id}')
    user_detail = [i for i in cursor]
    if not user_detail:
        raise Exception("id not found")
    else:
        query = f"DELETE FROM cart WHERE user_id = %d AND book_id = %d" %(user_id,book_id)
        cursor.execute(query)
        connection.commit()
        return book_id


def update_quantity_of_book_in_cart(book_id, user_id, quantity):
    """
        desc: deleting book from cart
        param:  user_id, book_id
        :return: quantity
    """
    cursor.execute(f'select user_id from cart where user_id={user_id}')
    user_detail = [i for i in cursor]
    if not user_detail:
        raise Exception("id not found")
    else:
        query = f"UPDATE cart SET quantity = %d WHERE book_id = %d AND user_id = %d" %(quantity,book_id,user_id)
        cursor.execute(query)
        connection.commit()
        return quantity

