from utils.db import db
from uuid import uuid4
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.String(16), unique=True, default=lambda: str(uuid4().int)[0:16])
    username = db.Column(db.String(80), unique=True, nullable=False, index=True)  # Create an index on the username column
    email = db.Column(db.String(255), unique=True, nullable=False, index=True)  # Create an index on the email column
    password = db.Column(db.String(255), nullable=False)

    __table_args__ = (
        db.UniqueConstraint('username', 'email', name='unique_username_email'),  # Create a unique constraint on the username and email columns
    )

    def set_password(self, password):
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    def __repr__(self):
        return f"<User {self.username}>"