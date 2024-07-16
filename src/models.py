import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__='usuario'
    id=Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    lastName = Column(String(30), nullable=False)
    email = Column(String(50), nullable=False, unique=True)

favorite_character =relationship('FavoriteCharacter')
favorite_planet =relationship('FavoritePlanet')
favorite_vehicle =relationship('FavoriteVehicle')

class character(Base):
    __tablename__='character'
    id = Column(Integer,primary_key=True)
    name = Column(String(50), nullable=False)    

    favorite_character=relationship('FavoriteCharacter')


class Planet(Base):
    __tablename__='planet'
    id=Column(Integer,primary_key=True)
    name= Column(String(50),nullable=False)  
    
    favorite_planet = relationship ('FavoritePlanet')



class Vehicle(Base):
    __tablename__='vehicle'
    id =Column(Integer,primary_key=True)
    name=Column(String(50), nullable=False)   

    favorite_vehicle = relationship('FavoritePlanet')


class FavoriteCharacter(Base):
    __tablename__='favorite_character'
    id =Column(Integer,primary_key=True)  
    character_id=Column(Integer,ForeignKey('character.id'), nullable=False)
    usuario_id =Column(Integer,ForeignKey('usuario.id'),nullable=False)

    character= relationship('Character')
    usuario = relationship('Usuario')


class FavoriteVehicle(Base):
    __tablename__='favorite_vehicle'
    id =Column(Integer,primary_key=True)
    Vehicle_id=Column(Integer,ForeignKey('vehicle.id'),nullable=False)
    usuario_id =Column(Integer,ForeignKey('usuario.id'),nullable=False)

    vehicle=relationship('Vehicle')
    usuario=relationship('Usuario')

class FavoritePlanet(Base):
    __tablename__='favorite_planet'
    id =Column(Integer,primary_key=True)
    planet_id=Column(Integer,ForeignKey('planet.id'), nullable=False)
    usuario_id =Column(Integer,ForeignKey('usuario.id'),nullable=False)

    planet=relationship('Planet')
    usuario=relationship('Usuario')



try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
