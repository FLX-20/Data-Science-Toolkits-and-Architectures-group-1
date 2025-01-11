import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay, confusion_matrix
from tensorflow.keras.preprocessing import image as keras_image
import numpy as np
import os
from app_config import IMAGE_SAVE_PATH
import os
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix


def evaluate_model(model, x_test, y_test):
    score = model.evaluate(x_test, y_test, verbose=0)
    print("Test loss:", score[0])
    print("Test accuracy:", score[1])


def plot_confusion_matrix(classifier, test_data, test_labels, batch_size=128):
    print("Plotting confusion matrix...")
    print("Test data shape:", test_data.shape)

    test_labels = np.argmax(test_labels, axis=1)

    all_predictions = []

    for start_idx in range(0, len(test_data), batch_size):
        end_idx = start_idx + batch_size
        batch_data = test_data[start_idx:end_idx]
        batch_predictions = classifier.predict(batch_data)
        all_predictions.extend(np.argmax(batch_predictions, axis=1))

    all_predictions = np.array(all_predictions)

    print("Confusion matrix:")
    cm = confusion_matrix(test_labels, all_predictions)

    _, ax = plt.subplots(figsize=(12, 12))
    ConfusionMatrixDisplay(cm).plot(cmap="Blues", ax=ax)

    print("Saving confusion matrix...")

    os.makedirs(IMAGE_SAVE_PATH, exist_ok=True)
    file_path = os.path.join(IMAGE_SAVE_PATH, "confusion_matrix.png")
    plt.title("Normalized Confusion Matrix")
    plt.savefig(file_path)

    print("Confusion matrix saved as confusion_matrix.png")
