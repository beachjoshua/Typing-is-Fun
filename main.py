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

# sends json of the data to the frontend at localhost:5000/api/weather

def main() -> None:
    print("test")

if __name__ == "__main__":
    app.run(debug=True)


