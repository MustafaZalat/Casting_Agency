import os 
from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import Movie, Actor, db, setup_dp
from auth import AuthError, requires_auth
from flask_migrate import Migrate


# create and config the app
 
def create_app(test_config=None):
    app = Flask(__name__)
    setup_dp(app)
    CORS(app)


    @app.after_request
    def after_request(response): 
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization, true')
        response.headers.add('Access-Control-Allow-Methods', 'GET, PATCH, POST, DELETE, OPTIONS')
        return response


    # create an api to get whole actors
    @app.route('/actors')
    @requires_auth('view:actors')
    def get_actors():
        try:
            all_actors = Actor.query.order_by(Actor.id).all()
            actors = [actor.format() for actor in all_actors]
            return jsonify ({
                'success' : True,
                'all_actors' : actors
            }),200

        except : 
            abort(422)

    # create an api to get whole movies
    @app.route('/movies')
    @requires_auth('view:movies')
    def get_movies():
        try:
            all_movies = Movie.query.order_by(Movie.id).all()
            movies = [movie.format() for movie in all_movies]
            return jsonify({
                'success' : True,
                'all_movies' : movies
            }),200

        except : 
            abort(422)


    # create an api create a new actor
    @app.route('/actors/create', methods=['POST'])
    @requires_auth('post:actor')
    def add_actor():
        body = request.get_json()
        name = body.get('name', None)
        age = body.get('age', None)
        gender = body.get('gender', None)
        movie_id = body.get('movie_id', None)

        try:
            actor = Actor(name=name, age=age, gender=gender, movie_id=movie_id)
            actor.insert()
            new_actor = actor.format()

            return ({
                'success' : True,
                'new_actor' : new_actor,
                'acotor_created' : actor.id
            }), 200 

        except:
            abort(422)


    # create an api create a new movie
    @app.route('/movies/create', methods=['POST'])
    @requires_auth('post:movie')
    def add_movie():
        body = request.get_json()
        title = body.get('title', None)
        release_date = body.get('release_date', None)
        actors = body.get('actors', None)


        try:
            movie = Movie(title=title, release_date=release_date, actors=actors)
            movie.insert()
            new_movie = movie.format()

            return ({
                'success' : True,
                'new_movie' : new_movie,
                'movie_created' : movie.id
            }), 200 

        except:
            abort(422)


    # create an api to delete actor
    @app.route('/actor/delete/<int:actor_id>', mothods = ['DELETE']) 
    @requires_auth('delet:actor')
    def delet_actor(actor_id):
        actor = Actor.query.order_by(Actor.id == actor_id).one_or_none()

        if actor is None:
            abort(404)

        try:
            actor.delete()
            db.session.commit()
            db.session.close()
            return({
                'success' : True,
                'delete' : actor_id,
                'message' : "actor  deleted successfully"
            }), 200 

        except:
            abort(422)


    # create an api to delete movie
    @app.route('/movie/delete/<int:movie_id>', mothods = ['DELETE'])
    @requires_auth('delete:movie')
    def delet_actor(movie_id):
        movie = Movie.query.order_by(Movie.id == movie_id).one_or_none()

        if movie is None:
            abort(404)

        try:
            movie.delete()
            db.session.commit()
            db.session.close()
            return({
                'success' : True,
                'delete' : movie_id,
                'message' : "movie deleted successfully"
            }), 200 

        except:
            abort(422)



    # create an api to edit actor info
    @app.route('/actor/edit/<int:actor_id>' , methods = ['PATCH'])
    @requires_auth('patch:actor')
    def edit_actor(actor_id):
        actor = Actor.query.filter(Actor.id == actor_id).one_or_none()
        body = request.get_json()
        name = body.get('name', None)
        age = body.get('age', None)
        gender = body.get('gender', None)
        movie_id = body.get('movie_id', None)

        if actor is None:
            abort (404)

        try: 
            actor.name = name
            actor.age = age
            actor.gender = gender
            actor.movie_id = movie_id
            actor.update()

            return ({
                'success' : True,
                'patch' : actor_id, 
                'message' : "actor updated seccessfuly"
            }), 200 

        except:
            abort(422)
        


    # create an api to edit movie info
    @app.route('/movie/edit/<int:movie_id>' , methods = ['PATCH'])
    @requires_auth('patch:movie')
    def edit_movie(movie_id):
        movie = Movie.query.filter(Movie.id == movie_id).one_or_none()
        body = request.get_json()
        title = body.get('title', None)
        release_date = body.get('release_date', None)

        if actor is None:
            abort (404)

        try: 
            movie.title = title
            movie.release_date = release_date
            
            movie.update()

            return ({
                'success' : True,
                'patch' : movie_id, 
                'message' : "movie updated seccessfuly"
            }), 200 

        except:
            abort(422)




    # implement error handlers using the @app.errorhandler(error)

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'error' : 404,
            'message' : 'Not Found'
        }), 404

    @app.errorhandler(422)
    def unprocessable_entity(error):
        return jsonify({
            'success': False,
            'error': 422,
            'message': 'bad request'
        })    
    return app
app = create_app()
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
