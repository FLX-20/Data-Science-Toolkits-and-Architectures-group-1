from flask import render_template, request, flash, redirect, url_for, render_template, Blueprint, jsonify
from .model import load_model
from .utils import allowed_file, process_image_and_predict
bp = Blueprint('routes', __name__)

model = load_model()


@bp.route('/')
def index():
    return render_template('index.html')


@bp.route('/api/predict', methods=['POST'])
def api_predict():

    if 'image' not in request.files:
        return jsonify({"error": "No image provided"}), 400

    img = request.files['image']
    if img.filename == '' or not allowed_file(img.filename):
        return jsonify({"error": "Invalid file type. Please upload an image."}), 400

    try:
        prediction, _ = process_image_and_predict(img, model)
        return jsonify({"prediction": prediction})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.route('/predict', methods=['POST'])
def web_predict():
    if 'image' not in request.files:
        flash("No image provided.", "danger")
        return redirect(url_for('routes.index'))

    img = request.files['image']
    if img.filename == '' or not allowed_file(img.filename):
        flash("Invalid file type. Please upload an image.", "warning")
        return redirect(url_for('routes.index'))

    try:
        prediction, image_path = process_image_and_predict(img, model)
        flash("Prediction successful!", "success")
        return render_template('index.html', prediction=prediction, image_url=image_path)
    except Exception as e:
        flash(f"An error occurred: {e}", "danger")
        return redirect(url_for('routes.index'))
