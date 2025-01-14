from keras import layers, Sequential, Input, models


def build_model_wandb(config, input_shape, num_classes):
    print(f"Input shape: {input_shape}")
    print(f"Num classes: {num_classes}")

    # Initialize the model
    model = models.Sequential()
    model.add(Input(shape=input_shape))

    # Add convolutional layers
    for i in range(config.conv_layers):
        model.add(layers.Conv2D(
            filters=config.conv_filters[i],
            kernel_size=tuple(config.kernel_sizes[i]),
            activation='relu'
        ))
        model.add(layers.MaxPooling2D(pool_size=tuple(config.pool_sizes[i])))

    # Add dropout and flatten
    model.add(layers.Dropout(config.dropout_rate))
    model.add(layers.Flatten())

    # Add fully connected layers
    for i in range(config.fc_layers):
        model.add(layers.Dense(config.fc_neurons[i], activation='relu'))

    # Add output layer
    model.add(layers.Dense(num_classes, activation='softmax'))

    return model
