import json
import os

MODELS_FILE = os.path.join(os.path.dirname(__file__), "../static/models.json")

def map_text_to_model(text):
    with open(MODELS_FILE, "r") as f:
        model_dict = json.load(f)

    for keyword, model_path in model_dict.items():
        if keyword in text:
            return model_path

    return "/example-assets/default.glb"  # fallback
