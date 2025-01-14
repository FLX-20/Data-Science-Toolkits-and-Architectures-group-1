import os
import numpy as np
import json
import tensorflow as tf
import wandb
import uuid
from wandb.integration.keras import WandbMetricsLogger
from models import build_model_wandb
from db_operations import get_uuids, load_images_and_labels_by_uuids, execute_query
from save_load_models import load_model_from_keras, save_model
from evaluate import evaluate_model, plot_confusion_matrix
from app_config import DATASET_PATH, DATASET_NAME, MODEL_NAME


def test_model():
    testing_uuids = get_uuids(is_training=0)
    model = load_model_from_keras(MODEL_NAME)

    if not model:
        raise ValueError("Failed to load the model.")

    test_images, test_labels = load_images_and_labels_by_uuids(
        testing_uuids, os.path.join(DATASET_PATH, DATASET_NAME)
    )

    test_dataset = create_tf_dataset(test_images, test_labels)

    print("Predicting labels on the test dataset...")
    predictions = model.predict(test_dataset)
    predicted_labels = np.argmax(predictions, axis=1)

    label_names = [row[0] for row in execute_query(
        "SELECT DISTINCT label FROM input_data;", fetch=True)]

    for image_uuid, predicted_label_idx in zip(testing_uuids, predicted_labels):
        predicted_label = label_names[predicted_label_idx]
        id = str(uuid.uuid4())
        query = """
        INSERT INTO predictions (id, image_id, predicted_label, model_name)
        VALUES (%s, %s, %s, %s)
        """
        params = (id, image_uuid, predicted_label,
                  MODEL_NAME)
        execute_query(query, params)

    print("Predictions saved successfully.")

    print("Plotting confusion matrix")
    plot_confusion_matrix(model, test_dataset)
    evaluate_model(model, test_dataset)


def preprocess_image(image, label, img_height=28, img_width=28):
    img = tf.convert_to_tensor(image, dtype=tf.float32)
    img = tf.image.resize(img, [img_height, img_width])
    img = tf.image.rgb_to_grayscale(img)
    img = img / 255.0
    label = tf.cast(label, tf.int32)
    return img, label


def create_tf_dataset(images, labels, batch_size=32, img_height=28, img_width=28):

    dataset = tf.data.Dataset.from_tensor_slices((images, labels))
    dataset = dataset.map(lambda x, y: preprocess_image(x, y, img_height, img_width),
                          num_parallel_calls=tf.data.AUTOTUNE)
    dataset = dataset.shuffle(buffer_size=1000).batch(
        batch_size).prefetch(tf.data.AUTOTUNE)

    return dataset


def train_model_wandb():

    training_uuids = get_uuids(is_training=1)
    testing_uuids = get_uuids(is_training=0)

    train_images, train_labels = load_images_and_labels_by_uuids(
        training_uuids, os.path.join(DATASET_PATH, DATASET_NAME)
    )
    test_images, test_labels = load_images_and_labels_by_uuids(
        testing_uuids, os.path.join(DATASET_PATH, DATASET_NAME)
    )

    train_dataset = create_tf_dataset(train_images, train_labels)
    test_dataset = create_tf_dataset(test_images, test_labels)

    wandb_training(train_dataset, test_dataset)


def wandb_training(train_dataset, test_dataset):

    with open("architecutres/architectures.json", "r") as file:
        architectures = json.load(file)

    for arch in architectures:
        print(f"Training model: {arch['name']}")
        print(arch)

        wandb.init(project="cnn-training", name=arch['name'], config=arch)
        config = wandb.config
        print(config)

        model = build_model_wandb(
            config, input_shape=(28, 28, 1), num_classes=10
        )

        optimizer = tf.keras.optimizers.Adam(learning_rate=config.learning_rate) \
            if config.optimizer == "adam" else tf.keras.optimizers.SGD(learning_rate=config.learning_rate)
        model.compile(optimizer=optimizer,
                      loss="categorical_crossentropy", metrics=['accuracy'])

        history = model.fit(
            train_dataset,
            epochs=config.epochs,
            validation_data=test_dataset,
            callbacks=[WandbMetricsLogger()]
        )

        loss, accuracy = model.evaluate(test_dataset)
        print(f"Model: {arch['name']} - Loss: {loss}, Accuracy: {accuracy}")

        save_model(model, arch['name'])
        wandb.finish()
