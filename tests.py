import pytest
import tempfile

from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

from src.admin import wsgi as ad_wsgi
from src.admin import main as ad_main
from src.client import wsgi as cl_wsgi
from src.client import main as cl_main


@pytest.fixture(scope="function")
def mock_client():
    mock_app = cl_wsgi.create_app(db_path=tempfile.mkstemp()[1])
    mock_db = SQLAlchemy(mock_app.app)
    mock_ma = Marshmallow(mock_app.app)

    class Book(mock_db.Model):
        __tablename__ = 'Books'
        __table_args__ = {'extend_existing': True}
        book_id = mock_db.Column('BOOK_ID', mock_db.Integer, primary_key=True, autoincrement=True)
        name = mock_db.Column('NAME', mock_db.Text, nullable=False)
        author = mock_db.Column('AUTHOR', mock_db.Text, nullable=False)
        publisher = mock_db.Column('PUBLISHER', mock_db.Text, nullable=False)
        category = mock_db.Column('CATEGORY', mock_db.Text, nullable=False)
        available = mock_db.Column('AVAILABLE', mock_db.Boolean, nullable=False)
        current_borrow_id = mock_db.Column('CURRENT_BORROW_ID', mock_db.Integer, nullable=True)

    class BookSchema(mock_ma.SQLAlchemyAutoSchema):
        class Meta:
            model = Book
            load_instance = True
            sqla_session = mock_db.session

    class User(mock_db.Model):
        __tablename__ = 'Users'
        __table_args__ = {'extend_existing': True}
        user_id = mock_db.Column('USER_ID', mock_db.Integer, primary_key=True, autoincrement=True)
        email = mock_db.Column('EMAIL', mock_db.Text, nullable=False)
        first_name = mock_db.Column('FIRST_NAME', mock_db.Text, nullable=False)
        last_name = mock_db.Column('LAST_NAME', mock_db.Text, nullable=False)
        password = mock_db.Column('PASSWORD', mock_db.Text, nullable=False)

    class UserSchema(mock_ma.SQLAlchemyAutoSchema):
        class Meta:
            model = User
            load_instance = True
            sqla_session = mock_db.session

    class Borrow(mock_db.Model):
        __tablename__ = 'Borrows'
        __table_args__ = {'extend_existing': True}
        borrow_id = mock_db.Column('BORROW_ID', mock_db.Integer, primary_key=True, autoincrement=True)
        book_id = mock_db.Column('BOOK_ID', mock_db.Integer, nullable=False)
        user_id = mock_db.Column('USER_ID', mock_db.Integer, nullable=False)
        borrow_date = mock_db.Column('BORROW_DATE', mock_db.Date, nullable=True)
        duration = mock_db.Column('DURATION', mock_db.Integer, nullable=True)
        return_date = mock_db.Column('RETURN_DATE', mock_db.Date, nullable=True)

    class BorrowSchema(mock_ma.SQLAlchemyAutoSchema):
        class Meta:
            model = Borrow
            load_instance = True
            sqla_session = mock_db.session

    mock_db.create_all()
    return mock_db, Book, BookSchema, Borrow, BorrowSchema, User, UserSchema


@pytest.fixture(scope="function")
def mock_admin():
    mock_app = ad_wsgi.create_app(db_path=tempfile.mkstemp()[1])
    mock_db = SQLAlchemy(mock_app.app)
    mock_ma = Marshmallow(mock_app.app)

    class Book(mock_db.Model):
        __tablename__ = 'Books'
        __table_args__ = {'extend_existing': True}
        book_id = mock_db.Column('BOOK_ID', mock_db.Integer, primary_key=True, autoincrement=True)
        name = mock_db.Column('NAME', mock_db.Text, nullable=False)
        author = mock_db.Column('AUTHOR', mock_db.Text, nullable=False)
        publisher = mock_db.Column('PUBLISHER', mock_db.Text, nullable=False)
        category = mock_db.Column('CATEGORY', mock_db.Text, nullable=False)
        available = mock_db.Column('AVAILABLE', mock_db.Boolean, nullable=False)
        current_borrow_id = mock_db.Column('CURRENT_BORROW_ID', mock_db.Integer, nullable=True)

    class BookSchema(mock_ma.SQLAlchemyAutoSchema):
        class Meta:
            model = Book
            load_instance = True
            sqla_session = mock_db.session

    class User(mock_db.Model):
        __tablename__ = 'Users'
        __table_args__ = {'extend_existing': True}
        user_id = mock_db.Column('USER_ID', mock_db.Integer, primary_key=True, autoincrement=True)
        email = mock_db.Column('EMAIL', mock_db.Text, nullable=False)
        first_name = mock_db.Column('FIRST_NAME', mock_db.Text, nullable=False)
        last_name = mock_db.Column('LAST_NAME', mock_db.Text, nullable=False)
        password = mock_db.Column('PASSWORD', mock_db.Text, nullable=False)

    class UserSchema(mock_ma.SQLAlchemyAutoSchema):
        class Meta:
            model = User
            load_instance = True
            sqla_session = mock_db.session

    class Borrow(mock_db.Model):
        __tablename__ = 'Borrows'
        __table_args__ = {'extend_existing': True}
        borrow_id = mock_db.Column('BORROW_ID', mock_db.Integer, primary_key=True, autoincrement=True)
        book_id = mock_db.Column('BOOK_ID', mock_db.Integer, nullable=False)
        user_id = mock_db.Column('USER_ID', mock_db.Integer, nullable=False)
        borrow_date = mock_db.Column('BORROW_DATE', mock_db.Date, nullable=True)
        duration = mock_db.Column('DURATION', mock_db.Integer, nullable=True)
        return_date = mock_db.Column('RETURN_DATE', mock_db.Date, nullable=True)

    class BorrowSchema(mock_ma.SQLAlchemyAutoSchema):
        class Meta:
            model = Borrow
            load_instance = True
            sqla_session = mock_db.session

    mock_db.create_all()
    return mock_db, Book, BookSchema, Borrow, BorrowSchema, User, UserSchema


def test_admin_add_book(mock_client, mock_admin, mocker, monkeypatch):
    mock_db, Book, BookSchema, Borrow, BorrowSchema, User, UserSchema = mock_admin
    mock_ClientAPICallHandler = mocker.Mock(add_book=lambda x: f"Book: {x} added")
    monkeypatch.setattr(ad_main, "db", mock_db)
    monkeypatch.setattr(ad_main, "ClientAPICallHandler", mock_ClientAPICallHandler)

    books_init = Book.query.all()
    assert len(books_init) == 0

    book_dets, status = ad_main.add_book({
        "name": "The Philosoper's stone",
        "publisher": "Scholastica",
        "author": "J. K. Rowling",
        "category": "Fiction",
        "available": True
    })
    books_after_add = Book.query.all()
    assert books_after_add[0].publisher == "Scholastica"
    assert len(books_after_add) == 1
