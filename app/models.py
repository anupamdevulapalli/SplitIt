from app import db
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy


class SecUsers(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(250))
    # username = db.Column(db.String(250), nullable=True)
    email = db.Column(db.String(60), index=True, unique=True, nullable=False)
    # password = db.Column(db.String(250), nullable=True)
    # verification = db.Column(db.Integer, nullable=True, default='0')
    # rememberToken = db.Column(
    #     db.String(250),
    #     nullable=True,
    #     unique=True,
    # )
    # created_at = db.Column(db.DateTime, default=datetime.utcnow)
    # created_by = db.Column(db.String(250), nullable=True)
    # updated_at = db.Column(db.DateTime, default=datetime.utcnow)
    # updated_by = db.Column(db.String(250), nullable=True)
    # deleted_at = db.Column(db.DateTime, default=datetime.utcnow)
    # deleted_by = db.Column(db.String(250), nullable=True)

    def __repr__(self):
        return '<SecUsers {}>'.format(self.full_name)

    # def setPassword(self, password):
    #     self.password = password

    # def checkPassword(self, password):
    #     return check_password_hash(self.password, password)
    
    # @staticmethod
    # def get(user_id):
    #     user = SecUsers.query.filter_by(id=user_id).first()
    #     if not user:
    #         return None

    #     user = SecUsers(
    #         id=user.id, full_name=user.full_name, email=user.email
    #     )
    #     return user