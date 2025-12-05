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

# Route for WordRunner Game
@app.route("/WordRunner")
def wordrunner():
    return render_template("WordRunner.html")

# Route for Lessons
@app.route("/testLesson")
def testLesson():
    return render_template("testLesson.html")

# Route for World Map
@app.route("/levels")
def levelMap():
    return render_template("levelMap.html")

# Route for Rhythm Game
@app.route("/rhythm")
def rhythm_game():
    return render_template("rhythmGame.html")

def main() -> None:
    print("test")

if __name__ == "__main__":
    app.run(debug=True)


