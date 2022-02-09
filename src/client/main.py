import typing as t

from .models import Book
from .models import BookSchema
from .models import User
from .models import UserSchema


def get(
        book_id=None, publisher=None, category=None
) -> t.Tuple[list, int]:
    return [{"book_3e424": True}], 200


def borrow(book_id, duration) -> t.Tuple[str, int]:
    # set book to unavailable
    # call admin endpoint to update books
    return "Request approved", 200


# todo: implement this
# def return_book(book_id, duration) -> t.Tuple[str, int]:
#     # call admin endpoint to update books
#     return "Request approved", 200


def enrol(user_data: dict) -> t.Tuple[str, int]:
    # call admin endpoint to update users
    return "Enrolment successful", 200
