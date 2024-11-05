from config import save_path

def save_model(model):
    model.save(save_path)
    print(f"Model saved in SavedModel format at {save_path}")