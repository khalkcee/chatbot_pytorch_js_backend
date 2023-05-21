from flask import Flask, request, jsonify
from flask_cors import CORS
from chat import get_response

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["POST"])
def index():
    text = request.get_json().get("message")
    response = get_response(text)
    message = {"answer": response}
    response = jsonify(message)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

if __name__ == "__main__":
    app.run(debug=True)
