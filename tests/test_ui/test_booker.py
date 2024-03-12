from data.users import user1
from helpers.booker_service import Booker


def test_auth():
    booker = Booker()
    token = booker.auth(user=user1)
    assert token


def test_delete_book():
    booker = Booker()
    token = booker.auth(user=user1)
    response = booker.delete_book('1', token)
