import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from models import Actor, Movie, setup_db
from app import create_app
from models import db
import datetime





class CastingTestCase(unittest.TestCase):

    def setUp(self):
        '''define test variables and initialize app'''

        self.app = create_app()
        self.client = self.app.test_client
        setup_db(self.app)
        db.create_all()

        self.new_movie = {
            'title': 'Elmamr',
            'release_date' : datetime.date(2020, 3, 1),
        }

        self.new_actor = {
            'name': 'Amir karara',
            'age': 28,
            'gender': 'Male',
            'movie_id': 1
        }

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        pass


    # actors get endpoint test
    def test_get_actors(self):
        res = self.client().get('/actors')
        self.assertEqual(res.status_code, 200)


    def test_get_actors_failed(self):
        res = self.client().get('/actors')
        self.assertEqual(res.status_code, 404)

    # moviess get endpoint test
    def test_get_movies(self):
        res = self.client().get('/movies')
        self.assertEqual(res.status_code, 200)

    def test_get_movies_failed(self):
        res = self.client().get('/moviess')
        self.assertEqual(res.status_code, 404)

    # actor create endpoint test
    def test_create_actor(self):
        res = self.client().post('/actors/create', json=self.new_actor)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['new_actor']['name'], 'Amir karara')
    
    def test_create_actor_failed(self):
        res = self.client.post('/actors/create', json=self.new_actor)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(res.get_json()['success'], False)

    # movie create endpoint test
    def test_create_movie(self):
        res = self.client().post('/movies/create', json=self.new_movie)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['new_movie']['title'], 'Elmamr')
    
    def test_create_actor_failed(self):
        res = self.client.post('/movies/create', json=self.new_movie)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(res.get_json()['success'], False)

    # actor delete endpoint test
    def test_delete_actor(self):
        res = self.client().delete('/actors/delete/1')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
    
    def test_delete_actor_failed(self):
        res = self.client().delete('/actors/delete/1000')
        self.assertEqual(res.status_code, 404)

    # movie delete endpoint test
    def test_delete_movie(self):
        res = self.client().delete('/movies/delete/1')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
    
    def test_delete_movie_failed(self):
        res = self.client().delete('/movies/delete/1000')
        self.assertEqual(res.status_code, 404)

    # actor patch endpoint test
    def test_edit_actor(self):
        res = self.client().patch('/actors/edit/1', json=self.new_actor)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
    
    def test_edit_actor_failed(self):
        res = self.client().patch('/actors/edit/2000', json=self.new_actor)
        self.assertEqual(res.status_code, 404)

    # movie patch endpoint test
    def test_patch_movie(self):
        res = self.client().patch('/movies/edit/2', json=self.new_movie)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
    
    def test_patch_movie_fail(self):
        res = self.client().patch('/movies/edit/2000', json=self.new_movie)
        self.assertEqual(res.status_code, 404)
    


if __name__ == "__main__":
     unittest.main()