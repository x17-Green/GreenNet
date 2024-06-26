#!usr/bin/python3
# Device class model

from utils.db import db

class Device(db.Model):
    __tablename__ = "devices"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(200), nullable=True)