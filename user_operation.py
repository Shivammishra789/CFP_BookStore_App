'''
@author: Shivam Mishra
@date: 20-01-22 6:23 PM
@desc: Contains different methods to add, delete, update user in database
'''
from database_connection import DBConnection


class UserOperation:
    """
    Contains different methods to add, delete, update, and retrieve user details
    """

    connection = DBConnection().establish_connection()
    cursor = connection.cursor(dictionary=True)

    def get_all_user_details(self):
        """
            desc: get all user details
            return: user_details
        """
        self.cursor.execute('select * from user_details')
        user_details = [i for i in self.cursor]
        return user_details

    def get_single_user_detail(self,user_id):
        """
            desc: get single user detail
            return: user detail
        """
        if id == "":
            raise Exception("User Details cannot be fetched", "error: id can't be empty")
        self.cursor.execute(f'select * from user_details where user_id={user_id}')
        user_detail = [i for i in self.cursor]
        if not user_detail:
            raise Exception("User Details cannot be fetched", "error: id not found")
        else:
            return user_detail

    def add_user(self, email_id, password, full_name, mobile_no):
        """
            desc: add user to database
            param: email_id, password, full_name
            return: user detail
        """
        query = '''insert into user_details (email_id, password, full_name, mobile_no)
                   VALUES ('%s','%s', '%s','%s')''' % (email_id, password, full_name, mobile_no)
        self.cursor.execute(query)
        self.connection.commit()
        query2 = "select user_id from user_details where email_id='%s'" % email_id
        self.cursor.execute(query2)
        user_id = [i for i in self.cursor]
        return user_id

    def verify_existing_user(self, email_id, password):
        """
            desc: verify existing user from database
            param: email_id, password
            return: user id
        """
        query = "select user_id from user_details where email_id = '%s' AND password = '%s'" % (email_id, password)
        self.cursor.execute(query)
        user_id = [i for i in self.cursor]
        if not user_id:
            raise Exception("Incorrect User Details", "error: id not found")
        else:
            return user_id

    def delete_user(self, user_id):
        """
            desc: delete user from database
            param: id
            return: deleted user id
        """
        query = "delete from user_details where user_id = %d" % user_id
        self.cursor.execute(query)
        self.connection.commit()
        return user_id

    def update_user_detail(self, user_id, update_param, update):
        """
            desc: update employee name
            param: id, name
            return: updated detail in dict form
        """
        query = "update user_details set %s = '%s' where user_id = %d" % (update_param, update, user_id)
        self.cursor.execute(query)
        self.connection.commit()
        updated_detail = self.get_single_user_detail(user_id)
        return updated_detail
