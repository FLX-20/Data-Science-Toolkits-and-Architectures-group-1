import tarfile
import pathlib
import tensorflow as tf
import numpy as np
import config

def extract_dataset(data_path, extract_to):
 
    data_dir = pathlib.Path(data_path)
    extract_path = pathlib.Path(extract_to)
    
    if not data_dir.is_file():
        raise FileNotFoundError(f"Dataset file not found at {data_dir}")
    
    with tarfile.open(data_dir, "r:gz") as tar:
        tar.extractall(path=extract_path)
        top_level_folder = pathlib.Path(tar.getnames()[0]).parts[0]
    
    return extract_path / top_level_folder

def preprocess_images_and_labels(dataset):

    normalization_layer = tf.keras.layers.Rescaling(1./255)
    dataset = dataset.map(lambda x, y: (normalization_layer(x), tf.one_hot(y, config.num_classes)))
    
    images = []
    labels = []
    for img, label in dataset:
        images.append(img.numpy())
        labels.append(label.numpy())
    
    images = np.concatenate(images, axis=0)
    labels = np.concatenate(labels, axis=0)
    
    return images, labels

def load_dataset(
    data_path, 
    extract_to, 
    batch_size=32, 
    img_height=180, 
    img_width=180, 
    validation_split=0.2, 
    seed=10
):
    image_dir = extract_dataset(data_path, extract_to)
    
    train_ds = tf.keras.utils.image_dataset_from_directory(
        image_dir,
        validation_split=validation_split,
        subset="training",
        seed=seed,
        image_size=(img_height, img_width),
        batch_size=batch_size
    )

    val_ds = tf.keras.utils.image_dataset_from_directory(
        image_dir,
        validation_split=validation_split,
        subset="validation",
        seed=seed,
        image_size=(img_height, img_width),
        batch_size=batch_size
    )

    sample_image, _ = next(iter(train_ds))
    num_channels = sample_image.shape[-1]
    config.input_shape = (img_height, img_width, num_channels)

    # Get class names and calculate number of classes
    class_names = train_ds.class_names
    config.num_classes = len(class_names)

    # Preprocess images and labels
    x_train, y_train = preprocess_images_and_labels(train_ds)
    x_test, y_test = preprocess_images_and_labels(val_ds)
    
    print("x_train shape:", x_train.shape)
    print(x_train.shape[0], "train samples")
    print(x_test.shape[0], "test samples")

    return (x_train, y_train), (x_test, y_test)

