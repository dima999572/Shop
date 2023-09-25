from flask import Flask
from flask_migrate import Migrate 

from .models import init_app, db
from .routes import book_blueprint


app = Flask(__name__)
app.config['SECRET_KEY'] = 'dima999572'
# TODO: Find a good way of reference to db using relative path, not absolute path (earlier relative path did not work)
import os
db_relative_path = os.path.join(os.getcwd(), 'database', 'user.db')
print(db_relative_path)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_relative_path}'

init_app(app)
app.register_blueprint(book_blueprint)

migrate = Migrate(app, db)


if __name__ == '__main__':
    app.run(debug=True, port=5002)