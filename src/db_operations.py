import psycopg2
import uuid
from db_connection import create_connection


def create_table():

    query = """
    CREATE TABLE IF NOT EXISTS images (
    id UUID PRIMARY KEY,
    name TEXT,
    url TEXT,
    file_path TEXT);
    """
    try:
        conn, cursor = create_connection()
        cursor.execute(query)
        conn.commit()
        print("Cartoon table created successfully.")
    except (Exception, psycopg2.databaseError) as error:
        print("Error creating cartoon table:", error)
    finally:
        conn.close()


def insert_image_metadata(name, url, file_path):
    query = """
    INSERT INTO images (id, name, url, file_path)
    VALUES (%s, %s, %s, %s)
    """
    try:
        image_id = uuid.uuid4()  # Generate a UUID
        conn, cursor = create_connection()
        # Convert UUID to string
        cursor.execute(query, (str(image_id), name, url, file_path))
        conn.commit()
        print(f"Image metadata for {
              name} inserted successfully with ID {image_id}.")
    except Exception as error:
        print(f"Error inserting metadata for {name}:", error)
    finally:
        conn.close()
