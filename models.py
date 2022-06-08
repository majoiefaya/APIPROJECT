from pydantic import BaseModel
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship



class Student(BaseModel):
    nom:str
    prenom:str
    filiere:str
    age:int

class StudentMatri(BaseModel):
    nom:str
    prenom:str
    filiere:str
    age:int
    matricule:str


class Filiere(BaseModel):
    libelleFiliere:str

class classe(BaseModel):
    libelleClasse:str