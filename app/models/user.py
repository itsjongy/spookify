import re
from datetime import datetime

from flask_bcrypt import Bcrypt
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates

bcrypt = Bcrypt()
db = SQLAlchemy()

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    hashed_password = db.Column(db.String(255), nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    profile_picture = db.Column(db.LargeBinary)
    status = db.Column(db.String(120))
    status_expiration = db.Column(db.DateTime)
    bio = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Define relationship to playlists
    playlists = db.relationship('Playlist', backref='user', lazy=True)

    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.hashed_password, password)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'profile_picture': self.profile_picture,
            'email': self.email,
            'status': self.status,
            'bio': self.bio,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }

    @validates('email')
    def validate_email(self, key, email):
        if not email:
            raise ValueError('Email is required.')
        if len(email) > 255:
            raise ValueError('Email is too long.')
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError('Email is invalid.')
        return email
