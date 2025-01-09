import os
import psycopg2
import random
import numpy as np
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from db_connection import create_connection
from app_config import DATASET_PATH, IMAGE_SAVE_PATH


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
    CREATE TABLE IF NOT EXISTS input_data (
        id UUID PRIMARY KEY,
        label TEXT NOT NULL,
        dataset_name TEXT NOT NULL,
        is_training BOOLEAN DEFAULT TRUE
    );
    """
    execute_query(query)


def create_predictions_table():

    query = """
    CREATE TABLE IF NOT EXISTS predictions (
        id UUID PRIMARY KEY,
        image_id UUID NOT NULL REFERENCES input_data(id) ON DELETE CASCADE,
        predicted_label TEXT NOT NULL,
        model_name TEXT NOT NULL,
        prediction_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """
    execute_query(query)


def insert_image_metadata(image_id, label, dataset_name):

    query = """
    INSERT INTO input_data (id, label, dataset_name, is_training)
    VALUES (%s, %s, %s, %s)
    """
    params = (str(image_id), label, dataset_name, bool(True))

    execute_query(query, params)


def get_image_metadata_by_uuid(uuid_input):

    query = """
    SELECT id, label, dataset_name
    FROM input_data
    WHERE id = %s;
    """
    try:
        conn, cursor = create_connection()

        cursor.execute(query, (uuid_input,))
        result = cursor.fetchone()

        if result:
            metadata = {
                "id": result[0],
                "label": result[3],
                "dataset_name": result[4]
            }
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
    SELECT id, label FROM input_data
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
            "UPDATE input_data SET is_training = TRUE WHERE id = %s;",
            [(id_,) for id_ in training_ids]
        )
        cursor.executemany(
            "UPDATE input_data SET is_training = FALSE WHERE id = %s;",
            [(id_,) for id_ in testing_ids]
        )
        conn.commit()
        print("Data successfully split into training and testing with balanced classes.")
    except Exception as e:
        print(f"Error during data split: {e}")
    finally:
        conn.close()


def get_uuids(is_training=True):

    query = "SELECT id FROM input_data WHERE is_training = %s;"
    try:
        conn, cursor = create_connection()
        cursor.execute(query, (is_training,))
        rows = cursor.fetchall()
        return [row[0] for row in rows]
    except Exception as e:
        raise RuntimeError(f"Error fetching UUIDs: {e}")
    finally:
        conn.close()


def get_metadata_by_uuids(uuids):

    placeholders = ','.join(['%s'] * len(uuids))
    query = f"SELECT id, label, dataset_name FROM input_data WHERE id IN ({
        placeholders});"
    try:
        conn, cursor = create_connection()
        cursor.execute(query, tuple(uuids))
        return cursor.fetchall()
    except Exception as e:
        raise RuntimeError(f"Error fetching metadata: {e}")
    finally:
        conn.close()


def load_images_and_labels_by_uuids(uuids, dataset_path, img_height=28, img_width=28):

    images = []
    labels = []

    # Retrieve metadata
    placeholders = ','.join(['%s'] * len(uuids))
    query = f"SELECT id, label FROM input_data WHERE id IN ({placeholders});"
    try:
        conn, cursor = create_connection()
        cursor.execute(query, tuple(uuids))
        rows = cursor.fetchall()
    except Exception as e:
        raise RuntimeError(f"Error fetching image labels: {e}")
    finally:
        conn.close()

    # Load images and collect labels
    for uuid, label in rows:
        img_path = os.path.join(dataset_path, f"{uuid}.jpg")
        if not os.path.exists(img_path):
            print(f"Image has not been found for UUID {uuid}, skipping.")
            continue

        # Load and preprocess the image
        img = tf.keras.utils.load_img(
            img_path, target_size=(img_height, img_width))
        img_array = tf.keras.utils.img_to_array(img) / 255.0

        images.append(img_array)
        labels.append(label)

    # Encode labels
    label_names = sorted(set(labels))
    labels = np.array([label_names.index(label)
                      for label in labels])
    labels = tf.keras.utils.to_categorical(
        labels, len(label_names))

    # Convert images to numpy array
    images = np.array(images, dtype=np.float32)

    return images, labels


def fetch_image_metadata():
    query = """
    SELECT DISTINCT ON (label) id, label
    FROM input_data
    """
    execute_query(query)


def load_images_and_labels(metadata):
    images = []
    labels = []

    for image_id, label in metadata:
        image_path = os.path.join(DATASET_PATH, f"{image_id}.jpg")
        if os.path.exists(image_path):
            img = Image.open(image_path)
            images.append(np.array(img))
            labels.append(label)
        else:
            print(f"Image {image_id} not found at {image_path}, skipping.")

    return images, labels


def plot_images(images, labels):
    fig, axes = plt.subplots(1, len(images), figsize=(15, 5))
    for i, ax in enumerate(axes):
        ax.imshow(images[i], cmap="gray")
        ax.axis("off")
        ax.set_title(f"Class: {labels[i]}")
    return fig


def save_image_grid(fig, output_file):
    fig.savefig(output_file)
    print(f"Saved the image grid to {output_file}.")


def load_and_display_images():

    output_dir = IMAGE_SAVE_PATH
    os.makedirs(output_dir, exist_ok=True)

    metadata = fetch_image_metadata()
    images, labels = load_images_and_labels(metadata)

    fig = plot_images(images, labels)
    output_file = os.path.join(output_dir, "class_images.png")
    save_image_grid(fig, output_file)
