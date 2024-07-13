import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    apellido = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    fecha_de_subscripción = Column(Date, nullable=False)
    username = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)

class Login(Base):
    __tablename__ = 'login'
    id = Column(Integer, primary_key=True)
    fecha_login = Column(Date, nullable=False)
    user_id = Column(Integer, ForeignKey('usuario.id'))

class Personaje(Base):
    __tablename__ = 'personaje'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    color_de_ojos = Column(String(250), nullable=False)
    color_de_cabello = Column(String(250), nullable=False)

class Favorito_Personaje(Base):
    __tablename__ = 'favorito_personaje'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('usuario.id'))
    personaje_id = Column(Integer, ForeignKey('personaje.id'))    

class Planeta(Base):
    __tablename__ = 'planeta'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    diámetro = Column(String(250), nullable=False)
    población = Column(String(250), nullable=False)

class Favorito_Planeta(Base):
    __tablename__ = 'favorito_planeta'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('usuario.id'))
    planeta_id = Column(Integer, ForeignKey('planeta.id'))    

class Vehículo(Base):
    __tablename__ = 'vehículo'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    modelo = Column(String(250), nullable=False)
    capacidad_de_pasajero = Column(String(250), nullable=False)

class Favorito_vehículo(Base):
    __tablename__ = 'favorito_vehículo'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('usuario.id'))
    vehículo_id = Column(Integer, ForeignKey('vehículo.id'))    


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
