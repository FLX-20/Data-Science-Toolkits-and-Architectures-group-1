import matplotlib.pyplot as plt
import config
from sklearn.metrics import ConfusionMatrixDisplay, confusion_matrix
from tensorflow.keras.preprocessing import image as keras_image
import numpy as np


def evaluate_model(model, x_test, y_test):
    score = model.evaluate(x_test, y_test, verbose=0)
    print("Test loss:", score[0])
    print("Test accuracy:", score[1])
    plot_confusion_matrix(model, x_test, y_test)


def plot_confusion_matrix(classifier, test_data, test_labels):

    test_labels = np.argmax(test_labels, axis=1)
    predictions = np.argmax(classifier.predict(test_data), axis=1)

    cm = confusion_matrix(test_labels, predictions)
    fig, ax = plt.subplots(figsize=(12, 12))
    ConfusionMatrixDisplay(cm, display_labels=range(
        config.num_classes)).plot(cmap="Blues", ax=ax)
    plt.title("Normalized Confusion Matrix")
    plt.savefig("confusion_matrix.png")
    print("Confusion matrix saved as confusion_matrix.png")


def predict_image_label(model, image_path):

    input_shape = model.input_shape[1:3]
    color_mode = "grayscale" if model.input_shape[-1] == 1 else "rgb"

    img = keras_image.load_img(
        image_path, target_size=input_shape, color_mode=color_mode)
    img_array = keras_image.img_to_array(img)
    img_array = img_array.astype("float32") / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    predictions = model.predict(img_array)
    predicted_label = np.argmax(predictions, axis=1)[0]

    return predicted_label
