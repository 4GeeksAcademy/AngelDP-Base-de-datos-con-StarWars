from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    firstname = Column(String(50))
    lastname = Column(String(50))
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String(255), nullable=False)

    favorites = relationship("Favorites", back_populates="user")

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email
        }


class Favorites(db.Model):
    __tablename__ = "favorites"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    specie_id = Column(Integer, ForeignKey("specie.id"), nullable=True)
    vehicle_id = Column(Integer, ForeignKey("vehicle.id"), nullable=True)
    starship_id = Column(Integer, ForeignKey("starship.id"), nullable=True)
    people_id = Column(Integer, ForeignKey("people.id"), nullable=True)
    planet_id = Column(Integer, ForeignKey("planet.id"), nullable=True)

    user = relationship("User", back_populates="favorites")
    planet = relationship("Planet", back_populates="favorites")
    specie = relationship("Specie", back_populates="favorites")
    vehicle = relationship("Vehicle", back_populates="favorites")
    starship = relationship("Starship", back_populates="favorites")
    people = relationship("People", back_populates="favorites")

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "specie_id": self.specie_id,
            "vehicle_id": self.vehicle_id,
            "starship_id": self.starship_id,
            "people_id": self.people_id,
            "planet_id": self.planet_id
        }


class Planet(db.Model):
    __tablename__ = "planet"
    id = Column(Integer, primary_key=True)
    diameter = Column(Integer)
    gravity = Column(Float)
    name = Column(String(50))
    population = Column(Integer)
    terrain = Column(String(50))
    climate = Column(String(50))

    favorites = relationship("Favorites", back_populates="planet")

    def serialize(self):
        return {
            "id": self.id,
            "diameter": self.diameter,
            "gravity": self.gravity,
            "name": self.name,
            "population": self.population,
            "terrain": self.terrain,
            "climate": self.climate
        }


class Specie(db.Model):
    __tablename__ = "specie"
    id = Column(Integer, primary_key=True)
    hair_color = Column(String(50))
    height = Column(Float)
    name = Column(String(50))
    skin_color = Column(String(50))
    language = Column(String(50))
    average_life = Column(Integer)

    favorites = relationship("Favorites", back_populates="specie")

    def serialize(self):
        return {
            "id": self.id,
            "hair_color": self.hair_color,
            "height": self.height,
            "name": self.name,
            "skin_color": self.skin_color,
            "language": self.language,
            "average_life": self.average_life
        }


class Vehicle(db.Model):
    __tablename__ = "vehicle"
    id = Column(Integer, primary_key=True)
    consumable = Column(String(50))
    crew = Column(Integer)
    name = Column(String(50))
    passengers = Column(Integer)
    class_name = Column(String(50))
    cargo_cap = Column(Integer)

    favorites = relationship("Favorites", back_populates="vehicle")

    def serialize(self):
        return {
            "id": self.id,
            "consumable": self.consumable,
            "crew": self.crew,
            "name": self.name,
            "passengers": self.passengers,
            "class_name": self.class_name,
            "cargo_cap": self.cargo_cap
        }


class Starship(db.Model):
    __tablename__ = "starship"
    id = Column(Integer, primary_key=True)
    consumable = Column(String(50))
    crew = Column(Integer)
    name = Column(String(50))
    passengers = Column(Integer)
    class_name = Column(String(50))
    cargo_cap = Column(Integer)

    favorites = relationship("Favorites", back_populates="starship")

    def serialize(self):
        return {
            "id": self.id,
            "consumable": self.consumable,
            "crew": self.crew,
            "name": self.name,
            "passengers": self.passengers,
            "class_name": self.class_name,
            "cargo_cap": self.cargo_cap
        }


class People(db.Model):
    __tablename__ = "people"
    id = Column(Integer, primary_key=True)
    hair_color = Column(String(50))
    height = Column(Float)
    name = Column(String(50))
    skin_color = Column(String(50))
    eye_color = Column(String(50))
    gender = Column(String(50))

    favorites = relationship("Favorites", back_populates="people")

    def serialize(self):
        return {
            "id": self.id,
            "hair_color": self.hair_color,
            "height": self.height,
            "name": self.name,
            "skin_color": self.skin_color,
            "eye_color": self.eye_color,
            "gender": self.gender
        }
