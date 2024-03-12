from data.users import user1
from helpers.base_service import BaseServices


class Booker(BaseServices):

    # https://restful-booker.herokuapp.com/auth
    def auth(self, user):
        path = 'auth'
        response = self.post(path, user)
        return response['token']

    def delete_book(self, id, token):
        path = 'auth/' + id
        response = self.delete(path, token, 404)
        return response
