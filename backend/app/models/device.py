#!usr/bin/python3
# Device class model

from flask_sqlalchemy import SQLAlchemy, table

db = SQLAlchemy()

class Device(db.Model):
    __table__ = "devices"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(200), nullable=True)