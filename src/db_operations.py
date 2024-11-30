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


def get_image_metadata_by_uuid(uuid_input):
    query = """
    SELECT id, url, file_path, label, dataset_name
    FROM images
    WHERE id = %s;
    """
    try:
        conn, cursor = create_connection()

        cursor.execute(query, (uuid_input,))
        result = cursor.fetchone()

        # Check if result is None or has fewer columns than expected
        if result:

            # Map the result to a dictionary
            metadata = {
                "id": result[0],
                "url": result[1],
                "file_path": result[2],
                "label": result[3],
                "dataset_name": result[4]
            }
            print(f"Metadata found for UUID {uuid_input}: {metadata}")
            return metadata
        else:
            print(f"No metadata found for UUID {uuid_input}")
            return None

    except Exception as error:
        print(f"Error retrieving metadata for UUID {uuid_input}: {error}")
        return None
    finally:
        conn.close()
