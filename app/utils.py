from werkzeug.utils import secure_filename
import os
import numpy as np
from PIL import Image
from werkzeug.datastructures import FileStorage
import io
from .model import model_predict

ALLOWED_EXTENSIONS = {'jpg', 'jpeg'}


def process_image_and_predict(img, model):

    from .database import InputData, Predictions, db

    image_array = decode_image(img)

    prediction = model_predict(model, image_array)

    new_input = InputData(
        label="unknown",
        dataset_name="MNIST",
        is_training=False
    )
    db.session.add(new_input)
    db.session.commit()

    image_path = save_image_with_uuid(image_array, str(new_input.id))

    new_prediction = Predictions(
        image_id=new_input.id,
        predicted_label=str(prediction),
        model_name="MNIST_CNN"
    )
    db.session.add(new_prediction)
    db.session.commit()

    return prediction, image_path


def decode_image(data):
    if not isinstance(data, FileStorage):
        raise ValueError("Data is not a file storage object")

    img = Image.open(io.BytesIO(data.read()))
    img = img.resize((28, 28)).convert('L')
    return np.array(img) / 255.0


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def save_image_with_uuid(image_array, uuid):
    save_dir = os.path.join('app', 'static', 'datasets', 'MNIST')
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    filename = f"{uuid}.jpg"
    file_path = os.path.join(save_dir, filename)
    Image.fromarray((image_array * 255).astype('uint8')
                    ).convert('L').save(file_path)

    return os.path.join('static', 'datasets', 'MNIST', filename)
