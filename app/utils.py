import numpy as np
from PIL import Image
from werkzeug.datastructures import FileStorage
import io


def decode_image(data):
    if not isinstance(data, FileStorage):
        raise ValueError("Data is not a file storage object")

    img = Image.open(io.BytesIO(data.read()))
    img = img.resize((28, 28)).convert('L')
    return np.array(img) / 255.0
