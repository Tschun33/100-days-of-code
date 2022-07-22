

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def receive_data():
    global u_name, u_password
    if request.method == "POST":
        u_name = request.form.get("username")
        u_password = request.form.get("password")
    return render_template("login.html", username=u_name, password=u_password)



if __name__ == "__main__":
    app.run(debug=True)
