import os
from sqlalchemy import Column, String, Integer, Boolean, create_engine
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy
import json

DB_HOST = os.getenv('DB_HOST', 'localhost:5432')
DB_USER = os.getenv('DB_USER', 'student')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'student')
DB_NAME = os.getenv('DB_NAME', 'trivia')
DB_PATH = "postgres://{}:{}@{}/{}".format(DB_USER, DB_PASSWORD, DB_HOST, DB_NAME)

db = SQLAlchemy()

"""
setup_db(app)
    binds a flask application and a SQLAlchemy service
"""
def setup_db(app, database_path=DB_PATH):
    app.config["SQLALCHEMY_DATABASE_URI"] = DB_PATH
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


"""
User

"""
class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    given_name = Column(String)
    family_name = Column(String)
    nickname = Column(String)
    name = Column(String)
    picture = Column(String)
    locale = Column(String)
    updated_at = Column(String)
    email = Column(String)
    email_verified = Column(Boolean)
    sub = Column(String)
    Favorite_players = Column(ARRAY(relationship('Player')))

    def __init__(self, question, answer, category, difficulty):
        self.question = question
        self.answer = answer
        self.category = category
        self.difficulty = difficulty

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'question': self.question,
            'answer': self.answer,
            'category': self.category,
            'difficulty': self.difficulty
            }
    

"""
Player

"""
class Player(db.Model):
    __tablename__ = 'players'

    id = Column(Integer, primary_key=True)
    type = Column(String)

    def __init__(self, type):
        self.type = type

    def format(self):
        return {
            'id': self.id,
            'type': self.type
            }
    