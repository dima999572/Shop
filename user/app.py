from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from datetime import timedelta

import models 
from routes import user_blueprint


app = Flask(__name__)
app.config['SECRET_KEY'] = 'dima999572'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)
# TODO: Find a good way of reference to db using relative path, not absolute path (earlier relative path did not work)
import os
db_relative_path = os.path.join(os.getcwd(), 'database', 'user.db')
print(db_relative_path)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_relative_path}'

models.init_app(app)
app.register_blueprint(user_blueprint)

login_manager = LoginManager(app)


@login_manager.user_loader
def load_user(user_id):
    return models.User.get(user_id)


migrate = Migrate(app, models.db)


if __name__ == '__main__':
    app.run(debug=True)   