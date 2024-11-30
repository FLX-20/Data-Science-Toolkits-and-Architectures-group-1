# db_connection.py
import time
import psycopg2
import logging
from db_config import DB_SETTINGS


def create_connection():
    max_retries = 5
    for attempt in range(max_retries):
        try:
            logging.info(f"Attempting to connect to the database (Attempt {
                         attempt + 1}/{max_retries})...")
            conn = psycopg2.connect(**DB_SETTINGS)
            cursor = conn.cursor()
            logging.info("Database connection successful.")
            return conn, cursor
        except Exception as error:
            logging.error(f"Error connecting to the database: {error}")
            time.sleep(5)
    logging.critical("Database connection failed after retries.")
    raise ConnectionError(
        "Unable to establish database connection after retries.")
