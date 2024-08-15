from exts import db
from datetime import datetime


class UserModel(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    join_time = db.Column(db.DateTime, default=datetime.now)
    platforms = db.relationship('PlatformModel', backref='UserModel', lazy='dynamic')

    def __repr__(self):
        return '<UserModel %r>' % self.username


class PlatformModel(db.Model):
    __tablename__ = 'platform'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    platform = db.Column(db.String(100), nullable=False)
    account = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='SET NULL'))
    user = db.relationship('UserModel', backref='PlatformModel')

    def __repr__(self):
        return '<PlatformModel %r>' % self.platform
