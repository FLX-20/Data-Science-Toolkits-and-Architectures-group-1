def save_model(model, model_file_path):
    model.save(model_file_path)
    print(f"Model saved in SavedModel format at {model_file_path}")
