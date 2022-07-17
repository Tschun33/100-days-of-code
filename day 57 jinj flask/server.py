import datetime

import requests
from requests import *

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    year = datetime.datetime.now().strftime("%Y")
    return render_template("index.html", num=year)

@app.route("/guess/<name>")
def guess(name):
    parameters = {
        "name": name
    }
    r = requests.get("https://api.genderize.io", params=parameters)
    r.raise_for_status()
    gender = r.json()["gender"]
    probability = r.json()["probability"]
    return render_template("guess.html", gender=gender, prob=probability)



if __name__ == "__main__":
    app.run(debug=True)
