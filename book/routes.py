from flask import Blueprint, request, jsonify, make_response

from models import db, Book


book_blueprint = Blueprint('book_api_routes', __name__, url_prefix='/api/book/')


@book_blueprint.route('/all', methods=['GET'])
def get_all_books():
    all_books = Book.query.all()
    result = [book.serialize() for book in all_books]
    return make_response(jsonify({
        'message': 'Returning all books',
        'response': result
    }), 200)


@book_blueprint.route('/create', methods=['POST'])
def create_books():
    try:
        book = Book()
        book.name = request.form['name']
        book.slug = request.form['slug']
        book.price = request.form['price']
        book.image = request.form['image']

        db.session.add(book)
        db.session.commit()

        response = {
            'message': 'Book Created',
            'result': book.serialize()
        }
    except Exception as e:
        response = {
            'message': f'Error in creating book. {e}'
        }

    return jsonify(response)


@book_blueprint.route('/<slug>', methods=['GET'])
def book_details(slug):
    book = Book.query.filter_by(slug=slug).first()
    if book:
        return make_response(jsonify({
            'result': book.serialize()
        }), 200)
    else:
        return make_response(jsonify({
            'result': 'No books found'
        }), 404)
