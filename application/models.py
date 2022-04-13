from enum import unique
from .database import db


class Phrases(db.Model):
    __tablename__ = 'phrases'
    p_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String, nullable=False)

class NewWords(db.Model):
    __tablename__ = 'new_words'
    nw_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nw = db.Column(db.String, nullable=False, unique=True)
    nw_meaning = db.Column(db.String)
    nw_flang = db.Column(db.String)
    nw_description = db.Column(db.String)
    ex_1 = db.Column(db.String)
    ex_2 = db.Column(db.String)

class PhrasalVerbs(db.Model):
    __tablename__ = 'phrasal_verbs'
    pv_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    pv = db.Column(db.String, nullable=False, unique=True)
    pv_meaning = db.Column(db.String)
    pv_flang = db.Column(db.String)
    ex_1 = db.Column(db.String)
    ex_2 = db.Column(db.String)

