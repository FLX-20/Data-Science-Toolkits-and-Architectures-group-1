from flask import Blueprint, request, jsonify, current_app
from .model import load_model, model_predict
from .utils import decode_image
from .database import db, InputData, Predictions
bp = Blueprint('routes', __name__)

model = load_model()


@bp.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({"error": "No image provided"}), 400
    img = request.files['image']
    try:
        with current_app.app_context():
            image_array = decode_image(img)
            prediction = model_predict(model, image_array)

            new_input = InputData(
                label="unknown",
                dataset_name="MNIST",
                is_training=False
            )
            db.session.add(new_input)
            db.session.commit()

            new_prediction = Predictions(
                image_id=new_input.id,
                predicted_label=str(prediction),
                model_name="MNIST_CNN"
            )
            db.session.add(new_prediction)
            db.session.commit()

        return jsonify({"prediction": prediction})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
