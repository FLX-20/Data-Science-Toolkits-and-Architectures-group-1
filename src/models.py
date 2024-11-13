from keras import layers, Sequential, Input
import config

def build_mnist_cnn():
    model = Sequential([
        Input(shape=config.input_shape),
        layers.Conv2D(32, kernel_size=(3, 3), activation="relu"),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Conv2D(64, kernel_size=(3, 3), activation="relu"),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Flatten(),
        layers.Dropout(0.5),
        layers.Dense(config.num_classes, activation="softmax"),
    ])
    model.summary()
    return model