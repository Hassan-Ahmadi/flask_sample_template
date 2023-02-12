from flask_app import db
from sqlalchemy.sql import func
from datetime import datetime


class Device(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=True)
    type = db.Column(db.String(20), nullable=True)
