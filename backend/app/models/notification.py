#!usr/bin/python3
# Notification class model

from flask_sqlalchemy import SQLAlchemy, table

db = SQLAlchemy()

class Notification(db.Model):
    __table__ = "notifications"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    device_id = db.relationship('devices.id', backref=db.backref('notifications', lazy=True))
    notification_type = db.Column(db.String(255), nullable=False)
    message = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    read_at = db.Column(db.Boolean, default=False)

    threshold_type = db.Column(db.String(255), nullable=False)
    threshold_value = db.Column(db.Float, nullable=False)
    notification_frequency = db.Column(db.String(255), nullable=False)
    notification_status = db.Column(db.Boolean, default=False)
