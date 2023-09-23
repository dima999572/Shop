from ..app import app, db
from ..models import Book
import pytest


@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    client = app.test_client()

    with app.app_context():
        db.create_all()
        yield client
        db.session.remove()
        db.drop_all()


def test_create_book(client):
    response = client.post('/api/book/create', data={
        'name': 'Test book',
        'slug': 'test-book',
        'price': 10,
        'image': 'test.jpg'
    })
    assert response.status_code == 200
    assert Book.query.count() == 1