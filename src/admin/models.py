from .wsgi import db, ma


class Book(db.Model):
    __tablename__ = 'Books'
    __table_args__ = {'extend_existing': True}
    book_id = db.Column('BOOK_ID', db.Text, primary_key=True)
    name = db.Column('NAME', db.Text, nullable=False)
    publisher = db.Column('PUBLISHER', db.Text, nullable=False)
    category = db.Column('CATEGORY', db.Text, nullable=False)
    available = db.Column('AVAILABLE', db.Boolean, nullable=False)
    current_borrow_id = db.Column('CURRENT_BORROW_ID', db.Text)


class BookSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Book
        load_instance = True
        sqla_session = db.session


class User(db.Model):
    __tablename__ = 'Users'
    __table_args__ = {'extend_existing': True}
    user_id = db.Column('USER_ID', db.Text, primary_key=True)
    email = db.Column('EMAIL', db.Text, nullable=False)
    first_name = db.Column('FIRST_NAME', db.Text, nullable=False)
    last_name = db.Column('LAST_NAME', db.Text, nullable=False)
    password = db.Column('PASSWORD', db.Text, nullable=False)


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Book
        load_instance = True
        sqla_session = db.session


class Borrow(db.Model):
    __tablename__ = 'Borrows'
    __table_args__ = {'extend_existing': True}
    borrow_id = db.Column('BORROW_ID', db.Text, primary_key=True)
    book_id = db.Column('BOOK_ID', db.Text, nullable=False)
    user_id = db.Column('USER_ID', db.Text, nullable=False)
    borrow_date = db.Column('BORROW_DATE', db.Text, nullable=False)
    duration = db.Column('DURATION', db.Integer, nullable=False)
    return_date = db.Column('RETURN_DATE', db.Text, nullable=False)


class BorrowSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Book
        load_instance = True
        sqla_session = db.session


db.create_all()
