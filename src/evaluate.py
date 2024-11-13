import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay, confusion_matrix
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
    ConfusionMatrixDisplay(cm, display_labels=range(10)).plot(cmap="Blues", ax=ax)
    plt.title("Normalized Confusion Matrix")
    plt.savefig("confusion_matrix.png")
    print("Confusion matrix saved as confusion_matrix.png")