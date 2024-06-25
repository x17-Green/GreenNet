#!usr/bin/python3
# User class model

from flask_sqlalchemy import SQLAlchemy, table

db = SQLAlchemy()

class User(db.Model):
    __table__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)