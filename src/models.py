from keras import layers, Sequential, Input, models


def build_model_wandb(config, input_shape, num_classes):

    print(f"Input shape: {input_shape[1:4]}")
    print(f"Num classes: {num_classes}")
    model = models.Sequential()
    model.add(Input(shape=(input_shape[1:4])))

    for i in range(config['conv_layers']):
        print(f" config filter {config['conv_filters'][i]}")
        print(f" config kernel {config['kernel_sizes'][i]}")
        model.add(layers.Conv2D(
            config['conv_filters'][i],
            tuple(config['kernel_sizes'][i]),
            activation='relu'
        ))
        model.add(layers.MaxPooling2D(tuple(config['pool_sizes'][i])))

    model.add(layers.Dropout(config['dropout_rate']))
    model.add(layers.Flatten())

    for i in range(config['fc_layers']):
        model.add(layers.Dense(config['fc_neurons'][i], activation='relu'))

    model.add(layers.Dense(num_classes, activation='softmax'))

    return model


def build_cnn(input_shape, num_classes):
    model = Sequential([
        Input(shape=input_shape),
        layers.Conv2D(32, kernel_size=(3, 3), activation="relu"),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Conv2D(64, kernel_size=(3, 3), activation="relu"),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Flatten(),
        layers.Dropout(0.5),
        layers.Dense(num_classes, activation="softmax"),
    ])
    model.summary()
    return model
