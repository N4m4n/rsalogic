from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
# Single RSA function
def rsa(value, key, n):
    return pow(value, key, n)


@app.route("/rsa", methods=["POST"])
def rsa_route():
    data = request.json

    try:
        value = int(data["value"])   # message or cipher
        key = int(data["key"])       # e or d
        n = int(data["n"])

        result = rsa(value, key, n)

        return jsonify({
            "input": value,
            "output": result
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route("/")
def home():
    return "Simple RSA API running 🚀"


if __name__ == "__main__":
    app.run(debug=True)
