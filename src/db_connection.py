import psycopg2
from db_config import DB_SETTINGS


def create_connection():
    try:
        conn = psycopg2.connect(**DB_SETTINGS)
        cursor = conn.cursor()
        return conn, cursor
    except Exception as error:
        print("Error connecting to the database:", error)
        raise
