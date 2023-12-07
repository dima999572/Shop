from flask import Flask
from flask_migrate import Migrate 
from models import init_app, db
from routes import book_blueprint


app = Flask(__name__)
app.config['SECRET_KEY'] = 'dima999572'

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://postgresadmin:admin123@postgres-service:5432/postgresdb'

init_app(app)
app.register_blueprint(book_blueprint)

migrate = Migrate(app, db)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
