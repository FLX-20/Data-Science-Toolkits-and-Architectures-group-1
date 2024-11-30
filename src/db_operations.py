import psycopg2
from db_connection import create_connection


def create_table():
    query = """
    CREATE TABLE IF NOT EXISTS images (
        id UUID PRIMARY KEY,
        url TEXT NOT NULL,
        file_path TEXT NOT NULL,
        label TEXT NOT NULL,
        dataset_name TEXT NOT NULL
    );
    """
    try:
        conn, cursor = create_connection()
        cursor.execute(query)
        conn.commit()
        print("Image table created successfully.")
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error creating image table:", error)
    finally:
        conn.close()


def insert_image_metadata(image_id, url, file_path, label, dataset_name):
    query = """
    INSERT INTO images (id, url, file_path, label, dataset_name)
    VALUES (%s, %s, %s, %s, %s)
    """
    try:
        conn, cursor = create_connection()
        cursor.execute(query, (str(image_id), url,
                       file_path, label, dataset_name))
        conn.commit()
        print(f"Image metadata for {
              image_id} inserted successfully with ID {image_id}.")
    except Exception as error:
        print(f"Error inserting metadata for {image_id}:", error)
    finally:
        conn.close()
