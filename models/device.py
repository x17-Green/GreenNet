#!usr/bin/python3
# Device class model

from utils.db import db

# Device model
class Device(db.Model):
    __tablename__ = "devices"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    notification_thresholds = db.relationship('NotificationThreshold', backref='device', lazy=True)
    notification_settings = db.relationship('NotificationSetting', backref='device', lazy=True)
    notification_history = db.relationship('NotificationHistory', backref='device', lazy=True)