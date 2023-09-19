from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin


db = SQLAlchemy()


def init_app(app):
    db.app = app
    db.init_app(app)


class Book(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    slug = db.Column(db.String(255), unique=True, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    amount = db.Column(db.Integer, nullable=False, default=10)
    image = db.Column(db.String(255))


    def __repr__(self):
        return f'<book {self.id} {self.name}>'


    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'slug': self.slug,
            'price': self.price,
            'amount': self.amount,
            'image': self.image
        }
 