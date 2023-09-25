from flask import Flask
from flask_migrate import Migrate
from flask.sessions import SecureCookieSessionInterface
from flask_login import LoginManager
from datetime import timedelta

from .models import init_app, db, User
from .routes import user_blueprint


app = Flask(__name__)
app.config['SECRET_KEY'] = 'dima999572'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)
# TODO: Find a good way of reference to db using relative path, not absolute path (earlier relative path did not work)
import os
db_relative_path = os.path.join(os.getcwd(), 'database', 'user.db')
print(db_relative_path)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_relative_path}'

init_app(app)
app.register_blueprint(user_blueprint)

login_manager = LoginManager(app)
migrate = Migrate(app, db)


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()


@login_manager.request_loader
def load_user_from_request(request):
    api_key = request.headers.get('Authorization')
    if api_key:
        api_key = api_key.replace('Basic ', '', 1)
        user = User.query.filter_by(api_key=api_key).first()
        if user:
            return user
        else:
            return None
        

class CustomSessionInterface(SecureCookieSessionInterface):
    """Prevent creating session from API requests."""

    def save_session(self, *args, **kwargs):
        if g.get('login_via_header'):
            return
        return super(CustomSessionInterface, self).save_session(*args, **kwargs)


if __name__ == '__main__':
    app.run(debug=True, port=5001)   