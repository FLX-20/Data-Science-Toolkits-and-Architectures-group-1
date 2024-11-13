import config

def save_model(model):
    model.save(config.save_path)
    print(f"Model saved in SavedModel format at {config.save_path}")