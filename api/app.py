from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Hello, Vercel!"})

@app.route("/greet/<name>")
def greet(name):
    return jsonify({"message": f"Hello, {name}!"})

if __name__ == "__main__":
    app.run()
