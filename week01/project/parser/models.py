"""
Creates sqlite database schema.
"""
from flask import Flask
import logging
import os
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
base_dir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir, 'app.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

"""
Class to upload excel file 
"""
class Upload(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(50))
    data = db.Column(db.LargeBinary)

"""
Class for Summary Rolling MoM worksheet.  
"""
class Summary(db.Model):
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

    def __repr__(self):
        return f"{self.id}-{self.date}-{self.callsoffered}-{self.abandoned}-{self.fcr}-{self.dsat}-{self.dsat}"


class Voc(db.Model):
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
	
    def __repr__(self):
        return f"{self.id}-{self.date}-{self.promoters}-{self.passives}-{self.dectractors}"
