'''
@author: Shivam Mishra
@date: 23-01-22 1:27 PM
'''
from core.database_connection import DBConnection


class BooksOperation:
    """
     Contains different methods to add, delete, update, and retrieve book details
    """

    connection = DBConnection().establish_connection()
    cursor = connection.cursor(dictionary=True)

    def show_all_books(self):
        """
        desc: displaying the book details
        return: data_list containing all books details
        """
        query = "select * from books"
        self.cursor.execute(query)
        data_list = [i for i in self.cursor]
        print(data_list)
        if data_list:
            return data_list
        else:
            raise Exception("table is not present in the database")

    def show_book_data(self, book_id):
        """
        desc: displaying the book_detail
        param: book_id
        return: data_list or error
        """
        query = "select * from books where id = %d" % book_id
        self.cursor.execute(query)
        data_list = [i for i in self.cursor]
        if data_list:
            return data_list
        else:
            raise Exception("this book id is not present in the database")

    def add_book_to_db(self, id, author, title, image, quantity, price, description):
        """
        desc: adding book details
        param : id, author, title, image, quantity, price, description
        return: book_details
        """
        query = '''insert into books (id, author, title, image, quantity, price, description) values
                   (%d, '%s', '%s', '%s', %d ,%f,'%s')''' % (id, author, title, image, quantity, price, description)
        self.cursor.execute(query)
        self.connection.commit()
        book_details = self.show_book_data(id)
        return book_details

    def update_book_detail(self, book_id, update_param, update):
        """
            desc: update book detail
            param: book id, updating parameter, update
            return: updated detail in dict form
        """
        query = "update user_details set %s = '%s' where id = %d" % (update_param, update, book_id)
        self.cursor.execute(query)
        self.connection.commit()
        updated_detail = self.show_book_data(book_id)
        return updated_detail

    def delete_book(self, book_id):
        """
        desc: deleting book details from the database
        param: book_id
        """
        self.show_book_data(book_id)
        query = "delete from books where id = %d" % book_id
        self.cursor.execute(query)
        self.connection.commit()