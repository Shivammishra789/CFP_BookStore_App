'''
@author: Shivam Mishra
@date: 23-01-22 1:27 PM
'''

from io import StringIO
from core.database_connection import DBConnection
import pandas as pd


class BooksOperation:
    """
     Contains different methods to add, delete, update, and retrieve book details
    """

    connection = DBConnection().establish_connection()
    cursor = connection.cursor(dictionary=True)

    def show_all_books_data(self):
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

    def show_single_book_data(self, book_id):
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

    def add_single_book(self, id, author, title, image, quantity, price, description):
        """
        desc: adding book details in  the user table
        param : id, author, title, image, quantity, price, description
        return: result
        """
        query = '''insert into books (id, author, title, image, quantity, price, description) values
                   (%d, '%s', '%s', '%s', %d ,%f,'%s')''' % (id, author, title, image, quantity, price, description)
        self.cursor.execute(query)
        self.connection.commit()
        book_details = self.show_single_book_data(id)
        return book_details

    def update_book(self, book_id, id, author, title, image, quantity, price, description):
        """
        desc: updating  id, author, title, image, quantity, price, description in  the books table
        param:  id, author, title, image, quantity, price, description
        return: updated data or error
        """
        query = '''update books set id = %d, author = '%s', title='%s', image='%s',quantity=%d, price = %f,
                   description = '%s' where id = %d''' % (id, author, title, image, quantity, price, description, book_id)
        self.cursor.execute(query)
        self.connection.commit()
        updated_data = self.show_single_book_data(id)
        return updated_data

    def delete_book(self, book_id):
        """
        desc: deleting book details from the database
        param: book_id
        """
        query = "delete from books where id = %d" % book_id
        self.cursor.execute(query)
        self.connection.commit()

    def insert_to_database(self, csv_file):
        """
        desc: to read csv and upload it to database
        param: csv_file: path of csv file
        """
        books_dataframe = pd.read_csv(StringIO(str(csv_file.file.read(), 'utf-8')), encoding='utf-8')
        cols = ", ".join([str(i) for i in books_dataframe.columns.tolist()])
        for i, row in books_dataframe.iterrows():
            sql = "INSERT INTO books (" + cols + ") VALUES (" + "%s," * (len(row) - 1) + "%s)"
            self.cursor.execute(sql, tuple(row))
            self.connection.commit()
