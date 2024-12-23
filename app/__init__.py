import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import time
import logging

logging.basicConfig(level=logging.INFO)

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your-secret-key'

    app.config['SQLALCHEMY_DATABASE_URI'] = (
        "postgresql://"
        f"{os.getenv('POSTGRES_USER')}:{os.getenv(
            'POSTGRES_PASSWORD')}@db:5432/{os.getenv('DB_NAME')}"
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from .database import InputData, Predictions
    with app.app_context():
        retries = 5
        while retries:
            try:
                db.create_all()
                logging.info("Database tables created successfully.")
                break
            except Exception as e:
                retries -= 1
                logging.warning(f"Database connection failed: {
                                e}. Retrying...")
                time.sleep(5)
        else:
            logging.error("Failed to connect to the database after retries.")
            raise RuntimeError("Database initialization failed.")

        from .routes import bp as routes_bp
        app.register_blueprint(routes_bp)

    return app
