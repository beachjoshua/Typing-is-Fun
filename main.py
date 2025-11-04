from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
import requests
import traceback

app = Flask(__name__)
CORS(app)

# shows the html on main localhost page
@app.route("/")
def home():
    return render_template("index.html")

# Route for the second page
@app.route("/keyboardDemo2")
def page2():
    return render_template("keyboardDemo2.html")

def main() -> None:
    print("test")

if __name__ == "__main__":
    app.run(debug=True)


