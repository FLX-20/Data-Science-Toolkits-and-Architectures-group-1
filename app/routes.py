from flask import Blueprint, request, jsonify
from .model import load_model, model_predict
from .utils import decode_image
bp = Blueprint('routes', __name__)

model = load_model()


@bp.route('/predict', methods=['POST'])
def predict():

    if 'image' not in request.files:
        return jsonify({"error": "No image provided"}), 400
    img = request.files['image']
    try:
        image_array = decode_image(img)
        prediction = model_predict(model, image_array)
        return jsonify({"prediction": int(prediction)})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
