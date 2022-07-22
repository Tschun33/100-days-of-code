from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

from form import LoginForm

app = Flask(__name__)
Bootstrap(app)
import os
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["POST", "GET"])
def login():
    login_form = LoginForm()
    login_form.validate_on_submit()
    if request.method == "GET":
        return render_template("login.html", form=login_form)
    if request.method == "POST":
        if login_form.name.data == "admin@email.com" and login_form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")



if __name__ == '__main__':
    app.run(debug=True)