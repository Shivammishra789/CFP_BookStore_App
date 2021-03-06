'''
@author: Shivam Mishra
@date: 20-01-22 12:02 PM
@desc: Contains methods to encode and decode token
'''

import time
import jwt


class JwtHandler:

    @staticmethod
    def encode_token(user_id):
        """
            desc: this function will encode the payload into a token
            param: id: it is a user id
            return: token id
        """
        key = 'users@678$registered9090';
        payload = {"user_id": user_id, "expires": time.time() + 60000}
        token_id = jwt.encode(payload, key)
        return token_id

    @staticmethod
    def decode_token(token_id):
        """
            desc: this function will decode the token into a payload
            param: token_id: it is a token which is generated at the time of adding a user
            return: decoded user id
        """
        payload = jwt.decode(token_id, "users@678$registered9090", algorithms=["HS256"])
        user_dict = payload.get('user_id')
        return user_dict[0]["user_id"]

