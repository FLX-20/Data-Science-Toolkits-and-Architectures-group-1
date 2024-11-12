import tarfile
import pathlib
import tensorflow as tf
import matplotlib.pyplot as plt

def extract_dataset(data_path, extract_to):
 
    data_dir = pathlib.Path(data_path)
    extract_path = pathlib.Path(extract_to)
    
    if not data_dir.is_file():
        raise FileNotFoundError(f"Dataset file not found at {data_dir}")
    
    with tarfile.open(data_dir, "r:gz") as tar:
        tar.extractall(path=extract_path)
        top_level_folder = pathlib.Path(tar.getnames()[0]).parts[0]
    
    return extract_path / top_level_folder

def create_datasets(image_dir, batch_size=32, img_height=180, img_width=180, validation_split=0.2, seed=123):

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

    class_names = train_ds.class_names

    return train_ds, val_ds, class_names

def load_dataset(
    data_path, 
    extract_to, 
    batch_size=32, 
    img_height=180, 
    img_width=180, 
    validation_split=0.2, 
    seed=123
):
    image_dir = extract_dataset(data_path, extract_to)
    
    train_ds, val_ds, class_names = create_datasets(
        image_dir,
        batch_size=batch_size,
        img_height=img_height,
        img_width=img_width,
        validation_split=validation_split,
        seed=seed
    )

    total_images = len(list(image_dir.glob('**/*.jpg')))
    print(f"Total images found: {total_images}")
    print("Class names:", class_names)

    return train_ds, val_ds, class_names