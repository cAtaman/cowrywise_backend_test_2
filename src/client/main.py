import typing as t

import requests

from .models import Book
from .models import BookSchema
from .models import User
from .models import UserSchema
from .wsgi import db, bcrypt
from ..constants import ADMIN_HOST, ADMIN_PORT, SECRET_KEY


def get(
        book_id=None, publisher=None, category=None
) -> t.Tuple[list, int]:
    query = Book.query
    if book_id:
        query = query.filter_by(book_id=book_id)
    if publisher:
        query = query.filter_by(publisher=publisher)
    if category:
        query = query.filter_by(category=category)
    books_dict = BookSchema(many=True).dump(query.all())
    return [books_dict], 200


def borrow(book_id: int, duration: int) -> t.Tuple[str, int]:
    book = Book.query.filter_by(book_id=book_id).first()
    if book and book.available:
        book.available = False
        db.session.add(book)
        db.session.commit()
        # todo: call admin endpoint to update books
        # admin_handler = AdminAPICallHandler(ADMIN_HOST, ADMIN_PORT)
        # admin_handler.borrow_book(book_id, duration)
        return "Request approved", 200
    else:
        return "Sorry this book is unavailable at the moment", 404


def enrol(user_data: dict) -> t.Tuple[str, int]:
    new_user_dict = {
        "email": user_data.get("email"),
        "first_name": user_data.get("first_name"),
        "last_name": user_data.get("last_name"),
        "password": user_data.get("password")
    }
    if not all(new_user_dict.values()):
        return f"All of {new_user_dict.keys()} are required", 400

    email = new_user_dict["email"]
    password = new_user_dict["password"]
    user = User.query.filter_by(email=email).first()

    if user:
        return f"User with email {email} already exists", 400

    new_user_dict["password"] = bcrypt.generate_password_hash(password).decode('utf-8')
    new_user = UserSchema(new_user_dict).load()
    db.session.add(new_user)
    db.session.commit()
    # todo: call admin endpoint to update users
    # admin_handler = AdminAPICallHandler(ADMIN_HOST, ADMIN_PORT)
    # admin_handler.new_user(new_user_dict)
    return "Enrolment successful", 200


class AdminAPICallHandler:
    """To handle internal calls to Admin API"""
    host: str
    port: str
    scheme: str = "http"

    def __init__(self, host, port, scheme=None):
        self.host = host
        self.port = port
        self.scheme = scheme or self.scheme
        self.headers = {"secret": SECRET_KEY}
        self.base_url = f"{self.scheme}://{self.host}:{self.port}/"

    def borrow_book(self, book_id, duration, user_id):
        url = self.base_url + "books"
        params = {"book_id": book_id, "duration": duration, "user_id": user_id}
        resp = requests.post(url, params=params, headers=self.headers)
        return resp

    def new_user(self, user_data):
        url = self.base_url + "users"
        resp = requests.post(url, json=user_data, headers=self.headers)
        return resp
