from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from chat import get_response
CORS(app, resources={r"/*": {"origins": "*"}})

 Access-Control-Allow-Origin: *
app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
    return "Welcome to the Chatbot API"

@app.route("/predict", methods=["POST"])
def predict():
    text = request.get_json().get("message")
    # TODO: check if text is valid
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)

if __name__ == "__main__":
    app.run(debug=True)
