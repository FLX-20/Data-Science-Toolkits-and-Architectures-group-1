import os
import time
import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

db = SQLAlchemy()


def create_app():

    app = Flask(__name__)

    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default-secret-key')

    db_user = os.getenv('POSTGRES_USER')
    db_password = os.getenv('POSTGRES_PASSWORD')
    db_name = os.getenv('DB_NAME')
    if not all([db_user, db_password, db_name]):
        raise RuntimeError("Missing required database environment variables: "
                           "POSTGRES_USER, POSTGRES_PASSWORD, DB_NAME.")

    app.config['SQLALCHEMY_DATABASE_URI'] = (
        f"postgresql://{db_user}:{db_password}@db:5432/{db_name}"
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from .routes import bp as routes_bp
    app.register_blueprint(routes_bp)

    initialize_database(app)

    return app


def initialize_database(app):

    with app.app_context():
        retries = 5
        while retries > 0:
            try:
                db.create_all()
                logging.info("Database tables created successfully.")
                break
            except Exception as e:
                retries -= 1
                logging.warning(f"Database connection failed: {
                                e}. Retrying in 10 seconds...")
                time.sleep(10)
        else:
            logging.error(
                "Failed to initialize the database after multiple retries.")
            raise RuntimeError("Database initialization failed.")
