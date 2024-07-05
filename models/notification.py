#!usr/bin/python3
# Notification class model

from utils.db import db

# Notification model
class Notification(db.Model):
    __tablename__ = "notifications"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    device_id = db.Column(db.Integer, db.ForeignKey('devices.id'), nullable=False)
    notification_type = db.Column(db.String(255), nullable=False)
    message = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    read_at = db.Column(db.Boolean, default=False)
    notification_history = db.relationship('NotificationHistory', backref='notification', lazy=True)