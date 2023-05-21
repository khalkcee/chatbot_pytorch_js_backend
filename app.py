from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from chat import get_response

app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
    return "Welcome to the Chatbot API"

@app.route("/predict", methods=["POST"])
def predict():
    text = request.get_json().get("message")
  
    response = jsonify(message)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

if __name__ == "__main__":
    app.run(debug=True)
