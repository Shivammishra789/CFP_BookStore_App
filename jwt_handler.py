'''
@author: Shivam Mishra
@date: 20-01-22 12:02 PM
@desc: Contains methods to encode and decode token
'''
import datetime
import jwt


class JwtHandler:

    @staticmethod
    def encode_token(id):
        """
            desc: this function will encode the payload into a token
            param: id: it is an user id
            return: token id
        """
        payload = {"user_id": id, "expiry": datetime.timedelta(days=1)}
        token_id = jwt.encode(payload, "users@678$registered9090")
        return token_id

    @staticmethod
    def decode_token(token_id):
        """
            desc: this function will decode the token into a payload
            param: token_id: it is a token which is generated at the time of adding an employee
            return: decoded employee id
        """
        payload = jwt.decode(token_id, "users@678$registered9090", algorithms=["HS256"])
        return payload.get('user_id')
