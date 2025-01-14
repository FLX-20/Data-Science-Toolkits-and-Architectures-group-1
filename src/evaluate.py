import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay, confusion_matrix, accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report
from tensorflow.keras.preprocessing import image as keras_image
import numpy as np
import os
from app_config import IMAGE_SAVE_PATH
import os
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix


def evaluate_model(model, test_dataset):
    y_pred = []
    y_true = []

    for images, labels in test_dataset:
        predictions = model.predict(images, verbose=0)
        y_pred.extend(np.argmax(predictions, axis=1))
        y_true.extend(np.argmax(labels.numpy(), axis=1))

    y_pred = np.array(y_pred)
    y_true = np.array(y_true)

    accuracy = accuracy_score(y_true, y_pred)
    precision = precision_score(y_true, y_pred, average='weighted')
    recall = recall_score(y_true, y_pred, average='weighted')
    f1 = f1_score(y_true, y_pred, average='weighted')

    print("Classification Report:")
    print(classification_report(y_true, y_pred))

    print(f"Accuracy: {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall: {recall:.4f}")
    print(f"F1 Score: {f1:.4f}")


def plot_confusion_matrix(classifier, dataset, batch_size=1000):

    all_predictions = []
    all_labels = []

    for batch_data, batch_labels in dataset:
        batch_predictions = classifier.predict(
            batch_data, batch_size=batch_size, verbose=0)
        all_predictions.extend(np.argmax(batch_predictions, axis=1))
        all_labels.extend(np.argmax(batch_labels.numpy(), axis=1))

    all_predictions = np.array(all_predictions)
    all_labels = np.array(all_labels)

    cm = confusion_matrix(all_labels, all_predictions)

    _, ax = plt.subplots(figsize=(12, 12))
    ConfusionMatrixDisplay(cm).plot(cmap="Blues", ax=ax)

    os.makedirs(IMAGE_SAVE_PATH, exist_ok=True)
    file_path = os.path.join(IMAGE_SAVE_PATH, "confusion_matrix.png")
    plt.title("Normalized Confusion Matrix")
    plt.savefig(file_path)
