from flask import Blueprint, jsonify, request, make_response
from flask_login import current_user, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

from models import db, User


user_blueprint = Blueprint('user_api_routes', __name__, url_prefix='/api/user/')


@user_blueprint.route('/all', methods=['GET'])
def get_all_users():
    all_user = User.query.all()
    result = [user.serialize() for user in all_user]
    return make_response(jsonify({
        'message': 'Returning all users',
        'response': result
    }), 200)


@user_blueprint.route('/create', methods=['POST'])
def create_user():
    try:
        user = User()
        user.username = request.form['username']
        user.password = generate_password_hash(request.form['password'], method='sha256')
        user.is_admin = True
        db.session.add(user)
        db.session.commit()

        response = {
            'message': 'User Created', 
            'result': user.serialize() 
        }

    except Exception as e:
        print(str(e))
        response = {
            'message': 'Error in creating response'
        }

    return jsonify(response)


@user_blueprint.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    user = User.query.filter_by(username=username).first()
    if not user:
        return make_response(jsonify({
            'message': 'Wrong username or password. Please check your credentials and try again.'
        }), 401)
    if check_password_hash(user.password, password):
        user.update_api_key()
        db.session.commit()
        login_user(user)
        return make_response(jsonify({
            'message': 'Logged in',
            'api_key': user.api_key
        }), 200)
    
    return make_response(jsonify({
        'message': 'Wrong username or password. Please check your credentials and try again.'
    }), 401)


@user_blueprint.route('/logout', methods=['POST'])
def logout():
    if current_user.is_authenticated:
        logout_user()
        return make_response(jsonify({
            'message': 'Logged out'
        }), 200)
    else:
        return make_response(jsonify({
            'message': 'No user logged in'
        }), 401)


@user_blueprint.route('/<username>/exist', methods=['GET'])
def user_exist(username):
    user = User.query.filter_by(username=username).first()
    if user:
        return make_response(jsonify({
            'result': True
        }), 200)
    else: 
        return make_response(jsonify({
            'result': False
        }), 404)


@user_blueprint.route('/', methods=['GET'])
def get_current_user():
    print(current_user.is_authenticated)
    if current_user.is_authenticated:
        return make_response(jsonify({
            'result': current_user.serialize()
        }), 200)
    else:
        return make_response(jsonify({
            'message': 'User not logged in'
        }), 401)