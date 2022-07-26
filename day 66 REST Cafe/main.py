from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        # Method 1.
        dictionary = {}
        # Loop through each column in the data record
        for column in self.__table__.columns:
            # Create a new dictionary entry;
            # where the key is the name of the column
            # and the value is the value of the column
            dictionary[column.name] = getattr(self, column.name)
        return dictionary

def str_to_bool(v):
    if v in ['True', ' true', 'T', 't', 'Yes', 'yes', 'y', '1']:
        return True
    else:
        return False


@app.route("/")
def home():
    return render_template("index.html")


## HTTP GET - Read Record
@app.route("/random")
def get_random_cafe():
    cafes = db.session.query(Cafe).all()
    random_cafe = random.choice(cafes)
    # return jsonify(cafe={
    #     "id": random_cafe.id,
    #     "name": random_cafe.name,
    #     "map_url": random_cafe.map_url,
    #     "img_url": random_cafe.img_url,
    #     "location": random_cafe.location,
    #     "seats": random_cafe.seats,
    #     "has_toilet": random_cafe.has_toilet,
    #     "has_wifi": random_cafe.has_wifi,
    #     "has_sockets": random_cafe.has_sockets,
    #     "can_take_calls": random_cafe.can_take_calls,
    #     "coffee_price": random_cafe.coffee_price,
    # })
    return jsonify(cafe=random_cafe.to_dict())


@app.route("/all")
def get_all():
    cafes = db.session.query(Cafe).all()
    return jsonify(cafes=[cafe.to_dict() for cafe in cafes])


@app.route("/search")
def get_cafe():
    location = request.args.get("loc")
    if location:
        search = db.session.query(Cafe).filter_by(location=f"{location}").all()

        return jsonify(cafes=[cafe.to_dict() for cafe in search])
    else:
        return {
            "error": {
                "Not Found": "Sorry, we dont have a cafe at that location."
            }
        }


## HTTP POST - Create Record

@app.route("/add", methods=["POST"])
def add_cafe():
    new_cafe = Cafe(
        name=request.args.get("name"),
        map_url=request.args.get("map_url"),
        img_url=request.args.get("img_url"),
        location=request.args.get("location"),
        seats=request.args.get("seats"),
        has_toilet=str_to_bool((request.args.get("has_toilet"))),
        has_wifi=str_to_bool((request.args.get("has_wifi"))),
        has_sockets=str_to_bool((request.args.get("has_sockets"))),
        can_take_calls=str_to_bool((request.args.get("can_take_calls"))),
        coffee_price=request.args.get("coffee_price"),
        )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe"})


## HTTP PUT/PATCH - Update Record

@app.route("/update_price/<cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    cafe_to_update = db.session.query(Cafe).filter_by(id=cafe_id).first()
    new_price = request.args.get("coffee_price")
    cafe_to_update.coffee_price = new_price
    db.session.commit()
    return jsonify(response={"success": "New price added"})

## HTTP DELETE - Delete Record

@app.route("/report_closed/<cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    if request.args.get("api-key") == "TopSecretAPIKey":
        cafe_to_delete = db.session.query(Cafe).filter_by(id=cafe_id).first()
        if cafe_to_delete:
            db.session.delete(cafe_to_delete)
            db.session.commit()
        else:
            return jsonify(response={"Not Found": "No Cafe with that id in database"})
        return jsonify(response={"success": "Cafe deleted"})
    else:
        return jsonify(response={"error": "Not allowed"})


if __name__ == '__main__':
    app.run(debug=True)
