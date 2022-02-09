"""This module handles response to system calls from the Client API"""
import typing as t
from datetime import datetime, timedelta

from .models import Book, Borrow, User, UserSchema
from .wsgi import db


def borrow(book_id: int, duration: int, user_id: int) -> t.Tuple[str, int]:
    # create a borrow entry
    new_borrow_dict = {
        "book_id": book_id,
        "user_id": user_id,
        "borrow_date": datetime.now().date(),
        "duration": duration,
        "return_date": datetime.now().date() + timedelta(duration)
    }
    new_borrow = Borrow(**new_borrow_dict)
    db.session.add(new_borrow)
    db.session.commit()

    # update book
    book = Book.query.filter_by(book_id=book_id).first()
    borrow = Borrow.query.filter_by(**new_borrow_dict).first()

    if not (book and borrow):
        return "Something went wrong", 404

    book.current_borrow_id = borrow.borrow_id
    book.available = False
    db.session.add(book)
    db.session.commit()
    return "Borrow successful", 200


def enrol(user_data: dict) -> t.Tuple[str, int]:
    new_user_dict = {
        "email": user_data.get("email"),
        "first_name": user_data.get("first_name"),
        "last_name": user_data.get("last_name"),
        "password": user_data.get("password")
    }
    email = new_user_dict["email"]
    user = User.query.filter_by(email=email).first()
    if user:
        return f"User with email {email} already exists", 400
    new_user = UserSchema().load(new_user_dict)
    db.session.add(new_user)
    db.session.commit()
    return "Enrolment successful", 200
