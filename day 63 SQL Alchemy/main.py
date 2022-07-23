from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

all_books = []



app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new_books_collection.db'
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'


db.create_all()


@app.route('/')
def home():
    all_books = db.session.query(Book).all()
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["POST", "GET"])
def add():
    if request.method == "GET":
        return render_template("add.html")
    if request.method == "POST":

        new_title = request.form["title"]
        new_author = request.form["author"]
        new_rating = request.form["rating"]
        new_book = Book(title=new_title, author=new_author, rating=new_rating)
        db.session.add(new_book)
        db.session.commit()
        all_books = db.session.query(Book).all()
        return render_template("index.html", books=all_books)


@app.route("/edit", methods=["POST", "GET"])
def edit():
    if request.method == "POST":
        book_id = request.form["id"]
        book_to_update = Book.query.get(book_id)
        book_to_update.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for("home"))
    book_id = request.args.get("id")
    book_selected = Book.query.get(book_id)
    return render_template("edit.html", book=book_selected)


@app.route("/delete")
def delete():
    book_id = request.args.get("id")
    Book.query.filter_by(id=book_id).delete()
    db.session.commit()
    return redirect(url_for("home"))



if __name__ == "__main__":
    app.run(debug=True)

