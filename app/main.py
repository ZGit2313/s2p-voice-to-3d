from flask import Flask, request, jsonify
from speech_to_3d_logic import map_text_to_model

app = Flask(__name__)

@app.route("/api/command", methods=["POST"])
def handle_command():
    data = request.json
    text_input = data.get("text", "").lower()

    if not text_input:
        return jsonify({"error": "No text provided"}), 400

    model_url = map_text_to_model(text_input)
    return jsonify({"model": model_url})

if __name__ == "__main__":
    app.run(debug=True)
