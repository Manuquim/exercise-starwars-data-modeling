import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String,DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    # Here we define columns for the table user
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), unique=True,nullable=False)
    email = Column(String(250),nullable=False)
    password= Column(String(250),unique=True, nullable=False)
    dis_date=Column(DateTime)
    planets = relationship("Planet", secondary="Colection")
    characters = relationship("Character", secondary="Colection")

class Planet(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table planets.
    # Notice that each column is also a normal Python instance attribute.
    id= Column(Integer, primary_key=True)
    planet_name = Column(String(250),unique=True,nullable=False)
    population=Column(Integer,unique=True)
    users = relationship("User", secondary="Colection")

class Character(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table characters.
    # Notice that each column is also a normal Python instance attribute.
    id= Column(Integer, primary_key=True)
    character_name = Column(String(250),unique=True,nullable=False)
    color_eyes=Column(String(25),unique=True)
    users = relationship("User", secondary="Colection")
    
    def to_dict(self):
        return {}

class Colection(Base):
    __tablename__ = 'colections'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer,ForeignKey('users.id'),nullable=False)
    planet_id = Column(Integer,ForeignKey('planets.id'))
    character_id=Column(Integer,ForeignKey('characters.id'))


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
