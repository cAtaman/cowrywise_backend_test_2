import typing as t

from .models import Book
from .models import BookSchema
from .models import Borrow
from .models import BorrowSchema
from .models import User
from .models import UserSchema


def get(available: bool = None) -> t.Tuple[t.List[dict], int]:
    return [{"book_id": "dfsafdasf"}], 200


def add_book(book_data: dict) -> t.Tuple[dict, int]:
    return {}, 200


def remove_book(book_data: dict) -> t.Tuple[dict, int]:
    return {}, 200

