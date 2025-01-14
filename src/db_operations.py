import os
import psycopg2
import random
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from PIL import Image
from db_connection import create_connection
from app_config import DATASET_PATH, IMAGE_SAVE_PATH, DATASET_NAME


def execute_query(query, params=None, fetch=False, fetchone=False):
    try:
        conn, cursor = create_connection()
        with conn, conn.cursor() as cursor:
            cursor.execute(query, params)
            if fetchone:
                return cursor.fetchone()
            if fetch:
                return cursor.fetchall()
            conn.commit()
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
        is_training SMALLINT DEFAULT 1
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


def insert_image_metadata(image_id, label, dataset_name, is_training):
    query = """
    INSERT INTO input_data (id, label, dataset_name, is_training)
    VALUES (%s, %s, %s, %s)
    """
    params = (str(image_id), label, dataset_name, is_training)
    execute_query(query, params)


def get_image_metadata_by_uuid(uuid_input):
    query = """
    SELECT id, label, dataset_name
    FROM input_data
    WHERE id = %s;
    """
    result = execute_query(query, (uuid_input,), fetchone=True)
    if result:
        return {"id": result[0], "label": result[1], "dataset_name": result[2]}
    print(f"No metadata found for UUID {uuid_input}")
    return None


def split_data_into_training_and_testing(validation_split=0.2, seed=24):
    query = "SELECT id, label FROM input_data WHERE is_training = 1 OR is_training = 0;"
    data = execute_query(query, fetch=True)

    from collections import defaultdict
    class_groups = defaultdict(list)
    for ids, class_label in data:
        class_groups[class_label].append(ids)

    training_ids = []
    testing_ids = []

    random.seed(seed)
    for ids in class_groups.values():
        random.shuffle(ids)
        split_idx = int(len(ids) * (1 - validation_split))
        training_ids.extend(ids[:split_idx])
        testing_ids.extend(ids[split_idx:])

    print(f"Training data: {len(training_ids)}")
    print(f"Testing data: {len(testing_ids)}")

    execute_query(
        "UPDATE input_data SET is_training = 1 WHERE id = ANY(%s::uuid[]);",
        (training_ids,)
    )
    execute_query(
        "UPDATE input_data SET is_training = 0 WHERE id = ANY(%s::uuid[]);",
        (testing_ids,)
    )

    print("Data successfully split into training and testing with balanced classes.")


def get_uuids(is_training=1):
    query = "SELECT id FROM input_data WHERE is_training = %s;"
    rows = execute_query(query, (is_training,), fetch=True)
    return [row[0] for row in rows]


def get_metadata_by_uuids(uuids):
    placeholders = ','.join(['%s'] * len(uuids))
    query = f"SELECT id, label, dataset_name FROM input_data WHERE id IN ({
        placeholders});"
    return execute_query(query, tuple(uuids), fetch=True)


def load_images_and_labels_by_uuids(uuids, dataset_path, img_height=28, img_width=28):
    images = []
    labels = []

    placeholders = ','.join(['%s'] * len(uuids))
    query = f"SELECT id, label FROM input_data WHERE id IN ({placeholders});"
    rows = execute_query(query, tuple(uuids), fetch=True)

    for uuid, label in rows:
        img_path = os.path.join(dataset_path, f"{uuid}.jpg")
        if not os.path.exists(img_path):
            print(f"Image has not been found for UUID {uuid}, skipping.")
            continue

        img = tf.keras.utils.load_img(
            img_path, target_size=(img_height, img_width))
        img_array = tf.keras.utils.img_to_array(img) / 255.0

        images.append(img_array)
        labels.append(label)

    label_names = sorted(set(labels))
    labels = np.array([label_names.index(label) for label in labels])
    labels = tf.keras.utils.to_categorical(labels, len(label_names))

    return np.array(images, dtype=np.float32), labels


def overview_image(output_file="overview.png", img_width=28, img_height=28):
    query = """
    SELECT DISTINCT ON (label) id, label
    FROM input_data
    """
    metadata = execute_query(query, fetch=True)

    print(metadata)

    if not metadata:
        print("No metadata found.")
        return

    images = []
    labels = []
    for image_id, label in metadata:
        image_path = os.path.join(
            DATASET_PATH, DATASET_NAME, f"{image_id}.jpg")
        if os.path.exists(image_path):
            try:
                img = Image.open(image_path).resize((img_width, img_height))
                images.append(img)
                labels.append(label)
            except Exception as e:
                print(f"Error loading image {image_id}: {e}")
        else:
            print(f"Image path not found for ID {image_id}: {image_path}")

    if not images:
        print("No images loaded.")
        return

    fig, axes = plt.subplots(1, len(images), figsize=(15, 5))
    for i, ax in enumerate(axes):
        ax.imshow(images[i], cmap="gray")
        ax.axis("off")
        ax.set_title(f"Label: {labels[i]}")

    output_path = os.path.join(IMAGE_SAVE_PATH, output_file)
    os.makedirs(IMAGE_SAVE_PATH, exist_ok=True)
    fig.savefig(output_path)
    plt.close(fig)

    print(f"Overview image saved at {output_path}")
