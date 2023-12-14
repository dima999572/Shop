from flask import Flask
from flask_migrate import Migrate
from models import db, init_app
from routes import order_blueprint


app = Flask(__name__)
app.config['SECRET_KEY'] = 'dima999572'

if os.environ.get('FLASK_ENV') == 'development':
    db_relative_path = os.path.join(os.getcwd(), 'database', 'order.db')
    print(db_relative_path)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_relative_path}'
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://postgresadmin:admin123@postgres-service:5432/postgresdb'


init_app(app)
app.register_blueprint(order_blueprint)

migrate = Migrate(app, db)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
