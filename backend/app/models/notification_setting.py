#!usr/bin/python3
# Notification Setting class model

from flask_sqlalchemy import SQLAlchemy, table

db = SQLAlchemy()

class NotificationSetting(db.Model):
    __table__ = "notification_settings"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    device_id = db.relationship('devices.id', backref=db.backref('notifications', lazy=True))
    notification_type = db.Column(db.String(255), nullable=False)
    enabled = db.Column(db.Boolean, nullable=False)
    frequency = db.Column(db.String(255), nullable=False)
