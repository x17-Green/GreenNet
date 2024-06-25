#!usr/bin/python3
# Device data class model

from flask_sqlalchemy import SQLAlchemy, table

db = SQLAlchemy()

class DeviceData(db.Model):
    __table__ = "device_data"
    id = db.Column(db.Integer, primary_key=True)
    device_id = db.Column(db.String(100), nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
