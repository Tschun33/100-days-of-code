from flask import Flask, render_template
from form import LoginForm

app = Flask(__name__)
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
    print(login_form.name.data)
    print(login_form.password.data)
    return render_template("login.html", form=login_form)


if __name__ == '__main__':
    app.run(debug=True)