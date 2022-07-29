import werkzeug.security
from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)


##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(255))
    name = db.Column(db.String(1000))



# Line below only required once, when creating DB.
# db.create_all()

@login_manager.user_loader
def load_user(user_id):
    return db.session.query(User).filter_by(id=user_id).first()

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=["POST", "GET"])
def register():
    if request.method == "POST":
        new_name = request.form.get("name")
        new_email = request.form.get("email")
        password = request.form.get("password")
        if db.session.query(User).filter_by(email=new_email).first():
            flash('Email already taken')
            return redirect("login")
        else:
            hashed_password = werkzeug.security.generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)
            new_user = User(
                name=new_name,
                email=new_email,
                password=hashed_password,
            )
            db.session.add(new_user)
            db.session.commit()
            print(check_password_hash(hashed_password, password))
            return redirect(url_for("login"))
    return render_template("register.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user_email = request.form.get("email")
        user_password = request.form.get("password")
        user = db.session.query(User).filter_by(email=user_email).first()
        if check_password_hash(user.password, user_password):
            login_user(user)
            flash('You were successfully logged in')
            return redirect(url_for('secrets'))
        else:
            error = "Invalid Credentials"
            flash(error)
            return redirect(url_for('login'))



    return render_template("login.html")


@app.route('/secrets')
@login_required
def secrets():
    print(current_user.name)
    return render_template("secrets.html", name=current_user.name, logged_in=True)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route('/download')
def download():
    return send_from_directory('static', filename="files/cheat_sheet.pdf")


if __name__ == "__main__":
    app.run(debug=True)
