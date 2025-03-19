from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    firstname = Column(String(50))
    lastname = Column(String(50))
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String(255), nullable=False)

    favorites = relationship("Favorite", back_populates="user")

    def serialize_user(self):
        return {
            "id": self.id,
            "username": self.username,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email
        }



class Favorite(db.Model):
    __tablename__ = "favorites"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    specie_id = Column(Integer, ForeignKey("species.id"), nullable=True)
    vehicle_id = Column(Integer, ForeignKey("vehicles.id"), nullable=True)
    starship_id = Column(Integer, ForeignKey("starships.id"), nullable=True)
    person_id = Column(Integer, ForeignKey("people.id"), nullable=True)
    planet_id = Column(Integer, ForeignKey("planets.id"), nullable=True)

    user = relationship("User", back_populates="favorites")
    planet = relationship("Planet", back_populates="favorites")
    specie = relationship("Specie", back_populates="favorites")
    vehicle = relationship("Vehicle", back_populates="favorites")
    starship = relationship("Starship", back_populates="favorites")
    person = relationship("Person", back_populates="favorites")

    def serialize_favorite(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "specie_id": self.specie_id,
            "vehicle_id": self.vehicle_id,
            "starship_id": self.starship_id,
            "person_id": self.person_id,
            "planet_id": self.planet_id
        }


class Planet(db.Model):
    __tablename__ = "planets"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    diameter = Column(Integer)
    gravity = Column(Float)
    population = Column(Integer)
    terrain = Column(String(100))
    climate = Column(String(100))

    favorites = relationship("Favorite", back_populates="planet")

    def serialize_planet(self):
        return {
            "id": self.id,
            "name": self.name,
            "diameter": self.diameter,
            "gravity": self.gravity,
            "population": self.population,
            "terrain": self.terrain,
            "climate": self.climate
        }


class Specie(db.Model):
    __tablename__ = "species"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    hair_color = Column(String(50))
    height = Column(Float)
    skin_color = Column(String(50))
    language = Column(String(50))
    average_life = Column(Integer)

    favorites = relationship("Favorite", back_populates="specie")

    def serialize_specie(self):
        return {
            "id": self.id,
            "name": self.name,
            "hair_color": self.hair_color,
            "height": self.height,
            "skin_color": self.skin_color,
            "language": self.language,
            "average_life": self.average_life
        }


class Vehicle(db.Model):
    __tablename__ = "vehicles"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    consumable = Column(String(50))
    crew = Column(Integer)
    passengers = Column(Integer)
    class_name = Column(String(50))
    cargo_cap = Column(Integer)
    terrain = Column(String(50))

    favorites = relationship("Favorite", back_populates="vehicle")

    def serialize_vehicle(self):
        return {
            "id": self.id,
            "name": self.name,
            "consumable": self.consumable,
            "crew": self.crew,
            "passengers": self.passengers,
            "class_name": self.class_name,
            "cargo_cap": self.cargo_cap,
            "terrain": self.terrain
        }


class Starship(db.Model):
    __tablename__ = "starships"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    consumable = Column(String(50))
    crew = Column(Integer)
    passengers = Column(Integer)
    class_name = Column(String(50))
    cargo_cap = Column(Integer)
    hyperdrive_rating = Column(Float)

    favorites = relationship("Favorite", back_populates="starship")

    def serialize_starship(self):
        return {
            "id": self.id,
            "name": self.name,
            "consumable": self.consumable,
            "crew": self.crew,
            "passengers": self.passengers,
            "class_name": self.class_name,
            "cargo_cap": self.cargo_cap,
            "hyperdrive_rating": self.hyperdrive_rating
        }


class Person(db.Model):
    __tablename__ = "people"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    hair_color = Column(String(50))
    height = Column(Float)
    skin_color = Column(String(50))
    eye_color = Column(String(50))
    gender = Column(String(50))

    favorites = relationship("Favorite", back_populates="person")

    def serialize_person(self):
        return {
            "id": self.id,
            "name": self.name,
            "hair_color": self.hair_color,
            "height": self.height,
            "skin_color": self.skin_color,
            "eye_color": self.eye_color,
            "gender": self.gender
        }