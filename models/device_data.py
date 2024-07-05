#!usr/bin/python3
# Device data class model

from utils.db import db

class DeviceData(db.Model):
    __tablename__ = "device_data"
    id = db.Column(db.Integer, primary_key=True)
    device_id = db.Column(db.String(100), nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    energy_consumption = db.Column(db.Float, nullable=False)
    energy_production = db.Column(db.Float, nullable=False)