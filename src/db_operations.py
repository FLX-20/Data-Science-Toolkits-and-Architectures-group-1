import os
import psycopg2
import random
from PIL import Image
from db_connection import create_connection


def execute_query(query, params=None):

    try:
        conn, cursor = create_connection()
        with conn, conn.cursor() as cursor:
            cursor.execute(query, params)
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error executing query: {error}")
    finally:
        if conn:
            conn.close()


def create_table():

    query = """
    CREATE TABLE IF NOT EXISTS images (
        id UUID PRIMARY KEY,
        url TEXT NOT NULL,
        label TEXT NOT NULL,
        dataset_name TEXT NOT NULL,
        is_training BOOLEAN NOT NULL DEFAULT TRUE
    );
    """
    execute_query(query)


def create_predictions_table():

    query = """
    CREATE TABLE IF NOT EXISTS image_predictions (
        id UUID PRIMARY KEY,
        image_id UUID NOT NULL REFERENCES images(id) ON DELETE CASCADE,
        predicted_label TEXT NOT NULL,
        model_name TEXT NOT NULL,
        prediction_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """
    execute_query(query)


def insert_image_metadata(image_id, url, label, dataset_name):

    query = """
    INSERT INTO images (id, url, label, dataset_name)
    VALUES (%s, %s, %s, %s)
    """
    params = (str(image_id), url, label, dataset_name)
    execute_query(query, params)


def get_image_metadata_by_uuid(uuid_input):
    query = """
    SELECT id, url, label, dataset_name
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
                "label": result[3],
                "dataset_name": result[4]
            }
            # print(f"Metadata found for UUID {uuid_input}: {metadata}")
            return metadata
        else:
            print(f"No metadata found for UUID {uuid_input}")
            return None

    except Exception as error:
        print(f"Error retrieving metadata for UUID {uuid_input}: {error}")
        return None
    finally:
        conn.close()


def split_data_into_training_and_testing(validation_split=0.2, seed=24):
    query = """
    SELECT id, label FROM images
    """
    try:
        conn, cursor = create_connection()
        cursor.execute(query)
        data = cursor.fetchall()

        # Group ids by class label
        from collections import defaultdict
        class_groups = defaultdict(list)
        for id_, class_label in data:
            class_groups[class_label].append(id_)

        training_ids = []
        testing_ids = []

        random.seed(seed)
        for class_label, ids in class_groups.items():
            random.shuffle(ids)
            split_idx = int(len(ids) * (1 - validation_split))
            training_ids.extend(ids[:split_idx])
            testing_ids.extend(ids[split_idx:])

        # Update the database
        cursor.executemany(
            "UPDATE images SET is_training = TRUE WHERE id = %s;",
            [(id_,) for id_ in training_ids]
        )
        cursor.executemany(
            "UPDATE images SET is_training = FALSE WHERE id = %s;",
            [(id_,) for id_ in testing_ids]
        )
        conn.commit()
        print("Data successfully split into training and testing with balanced classes.")
    except Exception as e:
        print(f"Error during data split: {e}")
    finally:
        conn.close()


def show_image(file_path):

    if not os.path.exists(file_path):
        print(f"Image file does not exist at path: {file_path}")
        return None

    try:
        image = Image.open(file_path)
        print(f"Image successfully loaded from {file_path}.")
        return image
    except Exception as error:
        print(f"Error loading image from {file_path}: {error}")
        return None
