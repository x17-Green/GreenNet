#!usr/bin/python3
# Notification History class model

from utils.db import db

class NotificationHistory(db.Model):
    __tablename__ = "notification_history"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    notification_id = db.Column(db.Integer, db.ForeignKey('notifications.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    device_id = db.relationship('devices.id', backref=db.backref('notifications', lazy=True))
    sent_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    read_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp(),\
        onupdate=db.func.current_timestamp())
    status = db.Column(db.String(50), nullable=False, default='unread')
    notification = db.relationship('Notifications', backref=db.backref('history', lazy=True))