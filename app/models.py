from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    role = db.Column(db.String(50), default='user') # user, researcher, developer, guru, admin

class GameObject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    color = db.Column(db.String(50), default='yellow')
    position_x = db.Column(db.Float, default=0.0)
    position_y = db.Column(db.Float, default=0.5)
    position_z = db.Column(db.Float, default=0.0)

class Telemetry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    event_type = db.Column(db.String(50)) # click, session_start, session_end
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())
    details = db.Column(db.String(255))
