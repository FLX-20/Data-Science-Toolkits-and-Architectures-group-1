from flask import Blueprint, request, jsonify
from .utils import decode_image
bp = Blueprint('routes', __name__)


@bp.route('/predict', methods=['POST'])
def predict():

    if 'image' not in request.files:
        return jsonify({"error": "No image provided"}), 400
    img = request.files['image']
    try:
        image_array = decode_image(img)
        print(image_array)
        return jsonify({"prediction": int(1)})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
