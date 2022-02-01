'''
@author: Shivam Mishra
@date: 23-01-22 1:27 PM
'''

from io import StringIO
from core.database_connection import DBConnection
from fastapi import HTTPException
import pandas as pd


class BooksOperation:
    """
     Contains different methods to add, delete, update, and retrieve book details
    """

    def show_all_books_data(self):
        """
        desc: displaying the book details
        return: data_list containing all books details
        """
        try:
            connection = DBConnection().establish_connection()
            cursor = connection.cursor(dictionary=True)
            query = "select * from books"
            cursor.execute(query)
            data_list = [i for i in cursor]
            if data_list:
                return data_list
            else:
                raise HTTPException(status_code=404, detail="No books available in database")
        finally:
            connection.close()

    def show_single_book_data(self, book_id):
        """
        desc: displaying the book_detail
        param: book_id
        return: data_list or error
        """
        try:
            connection = DBConnection().establish_connection()
            cursor = connection.cursor(dictionary=True)
            query = "select * from books where id = %d" % book_id
            cursor.execute(query)
            data_list = [i for i in cursor]
            if data_list:
                return data_list
            else:
                raise HTTPException(status_code=404, detail="this book id is not present in the database")
        finally:
            connection.close()

    def add_single_book(self, id, author, title, image, quantity, price, description):
        """
        desc: adding book details in  the user table
        param : id, author, title, image, quantity, price, description
        return: result
        """
        try:
            connection = DBConnection().establish_connection()
            cursor = connection.cursor(dictionary=True)
            query = '''insert into books (id, author, title, image, quantity, price, description) values
                       (%d, '%s', '%s', '%s', %d ,%f,'%s')''' % (id, author, title, image, quantity, price, description)
            cursor.execute(query)
            connection.commit()
            book_details = self.show_single_book_data(id)
            return book_details
        finally:
            connection.close()

    def update_book(self, book_id, id, author, title, image, quantity, price, description):
        """
        desc: updating  id, author, title, image, quantity, price, description in  the books table
        param:  id, author, title, image, quantity, price, description
        return: updated data or error
        """
        try:
            connection = DBConnection().establish_connection()
            cursor = connection.cursor(dictionary=True)
            query = "select id from books where id = %d" % book_id
            cursor.execute(query)
            data_list = [i for i in cursor]
            if data_list:
                query = '''update books set id = %d, author = '%s', title='%s', image='%s',quantity=%d, price = %f,
                                       description = '%s' where id = %d''' % (
                id, author, title, image, quantity, price, description, book_id)
                cursor.execute(query)
                connection.commit()
                updated_data = self.show_single_book_data(id)
                return updated_data
            else:
                raise HTTPException(status_code=404, detail="this book id is not present in the database")

        finally:
            connection.close()

    def delete_book(self, book_id):
        """
        desc: deleting book details from the database
        param: book_id
        """
        try:
            connection = DBConnection().establish_connection()
            cursor = connection.cursor(dictionary=True)
            cursor.execute(f'select id from books where id={book_id}')
            user_detail = [i for i in cursor]
            if not user_detail:
                raise Exception("Entered book id not found")
            else:
                query = "delete from books where id = %d" % book_id
                cursor.execute(query)
                connection.commit()
        finally:
            connection.close()

    def insert_to_database(self, csv_file):
        """
        desc: to read csv and upload it to database
        param: csv_file: path of csv file
        """
        try:
            connection = DBConnection().establish_connection()
            cursor = connection.cursor(dictionary=True)
            books_dataframe = pd.read_csv(StringIO(str(csv_file.file.read(), 'utf-8')), encoding='utf-8')
            cols = ", ".join([str(i) for i in books_dataframe.columns.tolist()])
            for i, row in books_dataframe.iterrows():
                sql = "INSERT INTO books (" + cols + ") VALUES (" + "%s," * (len(row) - 1) + "%s)"
                cursor.execute(sql, tuple(row))
                connection.commit()
        finally:
            connection.close()
