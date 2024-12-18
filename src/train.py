def train_model(model, x_train, y_train, batch_size=8, epochs=15):
    model.compile(loss="categorical_crossentropy",
                  optimizer="adam", metrics=["accuracy"])
    model.fit(x_train, y_train, batch_size=batch_size,
              epochs=epochs, validation_split=0.1)
