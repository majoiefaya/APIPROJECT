from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

class Student(Base): 
    __tablename__="Students"
    id=Column(Integer,primary_key=True,)
    nom= Column(String, index=True)
    prenom= Column(String, index=True)
    age= Column(Integer, index=True)
    dateNaiss=Column(String, index=True)
    filiere_id=Column(Integer, ForeignKey("Filiere.id"))
    classe_id=Column(Integer, ForeignKey("classe.id"))
    owner = relationship("Student")
    owner = relationship("Filiere", back_populates="Student")

class StudentMatri(Student):
    __tablename="StudentMatri"
    id=Column(Integer,primary_key=True,)
    matricule= Column(Integer, index=True)

class Filiere(Base):
    id=Column(Integer,primary_key=True,)
    __tablename="Filiere"
    libelle=Column(String, index=True)

class classe(Base):
    id=Column(Integer,primary_key=True,)
    tablename="classe"