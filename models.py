import os 
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer
import json
from flask_migrate import Migrate


database_filename = "database.db"
project_dir = os.path.dirname(os.path.abspath(__file__))
database_path = "sqlite:///{}".format(os.path.join(project_dir, database_filename))


db = SQLAlchemy()

def setup_dp(app):
    app.config["SQLALCHEMY_DATABASR_URI"] = database_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app 
    db.init_app(app)
    db.create_all()

class Movie(db.Model):
    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    release_date = db.Column(db.Date)
    actors = db.relationship('Actor', backref='movies', lazy=True)

    def __repr__(self):
        return f'<movies{self.id}{self.title}{self.release_date}{self.actors}'

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Actor(db.Model):
    __tablename__='actors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    age = db.Column(db.Integer)
    gender = db.Column(db.String)
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.id'), nullable=False)

    def __repr__(self):
        return f'<actors{self.id}{self.name}{self.age}{self.gender}{self.movie_id}'

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()