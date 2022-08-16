from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(256), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow) # Coordinated Universal Time (always save it to this time when storing, and convert it later on front end)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Save the password as the hashed version of the password
        self.password = generate_password_hash(kwargs['password'])
        db.session.add(self)
        db.session.commit()