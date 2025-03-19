"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, People, Starship, Vehicle, Specie, Planet
# from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace(
        "postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object


@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints


@app.route('/')
def sitemap():
    return generate_sitemap(app)


@app.route('/people', methods=['GET'])
def get_all_people():

    people = People.query.all()
    people_serialized = [people.serialize() for people in people]

    if not people:
        return jsonify({
            "msg": "Not found"
        }), 404

    return jsonify({
        "msg": "People succesfully",
        "people": people_serialized
    }), 200


@app.route('/people/<int:people_id>', methods=['GET'])
def get_person(people_id):

    person = People.query.get(people_id)

    if not person:
        return jsonify({
            "msg": "Not found"
        }), 404

    return jsonify({
        "msg": "person found",
        "people": person.serialize()
    }), 200


@app.route('/starships', methods=['GET'])
def get_all_starships():

    starships = Starship.query.all()
    starship_serialized = [starship.serialize() for starship in starships]

    if not starships:
        return jsonify({
            "msg": "Not found"
        }), 404

    return jsonify({
        "msg": "Starships succesfully",
        "starship": starship_serialized
    }), 200


@app.route('/starships/<int:starship_id>', methods=['GET'])
def get_starship(starship_id):

    starship = Starship.query.get(starship_id)

    if not starship:
        return jsonify({
            "msg": "Not found"
        }), 404

    return jsonify({
        "msg": "starship found",
        "starship": starship.serialize()
    }), 200


@app.route('/vehicles', methods=['GET'])
def get_all_vehicles():

    vehicles = Vehicle.query.all()
    vehicle_serialized = [vehicle.serialize() for vehicle in vehicles]

    if not vehicles:
        return jsonify({
            "msg": "Not found"
        }), 404

    return jsonify({
        "msg": "Vehicles succesfully",
        "vehicle": vehicle_serialized
    }), 200


@app.route('/vehicles/<int:vehicle_id>', methods=['GET'])
def get_vehicle(vehicle_id):

    vehicle = Vehicle.query.get(vehicle_id)

    if not vehicle:
        return jsonify({
            "msg": "Not found"
        }), 404

    return jsonify({
        "msg": "starship found",
        "vehicle": vehicle.serialize()
    }), 200


@app.route('/species', methods=['GET'])
def get_all_species():

    species = Specie.query.all()
    specie_serialized = [specie.serialize() for specie in species]

    if not species:
        return jsonify({
            "msg": "Not found"
        }), 404

    return jsonify({
        "msg": "Vehicles succesfully",
        "specie": specie_serialized
    }), 200


@app.route('/specie/<int:specie_id>', methods=['GET'])
def get_specie(specie_id):

    specie = Specie.query.get(specie_id)

    if not specie:
        return jsonify({
            "msg": "Not found"
        }), 404

    return jsonify({
        "msg": "starship found",
        "specie": specie.serialize()
    }), 200


@app.route('/planets', methods=['GET'])
def get_all_planets():

    planets = Planet.query.all()
    planet_serialized = [planet.serialize() for planet in planets]

    if not planets:
        return jsonify({
            "msg": "Not found"
        }), 404

    return jsonify({
        "msg": "Vehicles succesfully",
        "planet": planet_serialized
    }), 200


@app.route('/planets/<int:planet_id>', methods=['GET'])
def get_planet(planet_id):

    planet = Planet.query.get(planet_id)

    if not planet:
        return jsonify({
            "msg": "Not found"
        }), 404

    return jsonify({
        "msg": "starship found",
        "planet": planet.serialize()
    }), 200


@app.route('/users', methods=['GET'])
def get_all_users():

    users = User.query.all()

    return jsonify({
        "msg": "User retrived successfully",
        "users": [user.serialize() for user in users]
    }), 200


@app.route('/users/favorites/<int:user_id>', methods=["GET"])
def get_user_fav(user_id):

    user = User.query.get(user_id)

    if not user:
        return jsonify({
            "msg": "Not found"
        }), 404

    return jsonify({
        "msg": "User found succesfully",
        "favorite": user.serialize_favorites()
    }), 200


@app.route('/users', methods=['POST'])
def new_user():

    request_data = request.get_json()

    if not request_data.get('email') or not request_data.get('password') or not request_data.get('username'):
        return jsonify({
            "msg": "Email, password and username are required"
            }), 400

    existing_user = User.query.filter_by(email = request_data.get('email')).first()

    if existing_user:
        return jsonify({"msg": "User already exists"}), 403

    new_user = User(

        password = request_data["password"],
        username = request_data["username"],
        firstname = request_data["firstname"],
        lastname = request_data["lastname"],
        email = request_data["email"]
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({
        "msg" : "User created succesfully"
    }), 201


# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
