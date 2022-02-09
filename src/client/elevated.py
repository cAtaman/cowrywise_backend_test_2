"""This module handles response to system calls from Admin API"""
import typing as t

from .models import BookSchema, Book
from .wsgi import db


def add_book(book_data: dict) -> t.Tuple[dict, int]:
    book = BookSchema().load(book_data)
    db.session.add(book)
    db.session.commit()
    return BookSchema().dump(book), 200


def remove_book(book_id: int) -> t.Tuple[str, int]:
    book = Book.query.filter_by(book_id=book_id).first()
    if book:
        db.session.delete(book)
        db.session.commit()
        return "Book removed successfully", 200
    else:
        return "Book was not in catalogue", 400
