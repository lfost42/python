"""
Creates sqlite database schema.
"""
import os
from flask_sqlalchemy import SQLAlchemy
import app

db = SQLAlchemy(app)

base_dir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(base_dir, 'app.sqlite')
SQLALCHEMY_TRACK_MODIFICATIONS = False

class Upload(db.Model):
    """
    Class to upload excel file
    """
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(50))
    data = db.Column(db.LargeBinary)


class SummaryInfo(db.Model):
    """
    Class for Summary Rolling MoM worksheet properties.
    """
    __tablename__ = 'summary'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    callsoffered = db.Column(db.Integer, nullable=False)
    abandoned = db.Column(db.Float, nullable=False)
    fcr = db.Column(db.Float, nullable=False)
    dsat = db.Column(db.Float, nullable=False)
    csat = db.Column(db.Float, nullable=False)

    def __init__(self, date, callsoffered, abandoned, fcr, dsat, csat):
        self.date = date
        self.callsoffered = callsoffered
        self.abandoned = abandoned
        self.fcr = fcr
        self.dsat = dsat
        self.csat = csat


class VocInfo(db.Model):
    """
    Class for VOC Rolling MoM worksheet properties.
    """
    __tablename__ = 'voc'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    promoters = db.Column(db.Integer, nullable=False)
    passives = db.Column(db.Integer, nullable=False)
    dectractors = db.Column(db.Integer, nullable=False)

    def __init__(self, date, promoters, passives, dectractors):
        self.date = date
        self.promoters = promoters
        self.passives = passives
        self.dectractors = dectractors
