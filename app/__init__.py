from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '1234'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mnist.db'

    db.init_app(app)

    with app.app_context():
        from .routes import bp as routes_bp
        app.register_blueprint(routes_bp)

    return app
