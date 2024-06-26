#!usr/bin/python3
# Notification Threshold class model

from utils.db import db

class NotificationThreshold(db.Model):
    __tablename__ = "notification_thresholds"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    device_id = db.relationship('devices.id', backref=db.backref('notifications', lazy=True))
    threshold_type = db.Column(db.String(255), nullable=False)
    threshold_value = db.Column(db.Float, nullable=False)
    notification_frequency = db.Column(db.String(255), nullable=False)
    notification_status = db.Column(db.Boolean, default=False)