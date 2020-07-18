This project is the final project for the Udacity Full Stack Developer Nano Degree 

The project is to simulate a casting agency. This includes having actors and movies and assigning actors to movies. 

This project has two models/tables: A movie table that holds all the movies and an actors table that holds all the actors. For each movie, there are many actors so there is a one to many relationship there. 


to get to the heroku link: https://casting-agency-cap-udacity.herokuapp.com/ | https://git.heroku.com/casting-agency-cap-udacity.git


Database Url: DATABASE_URL: postgres://dxlowpykrkdozi:53fc5a00bb457405214bd2e5716e1f70e6c425b041302a8159c8f94f7fe78557@ec2-3-91-112-166.compute-1.amazonaws.com:5432/dbtp9e0jsiqsp0


To run the server, execute:

```
export FLASK_APP=api.py
export FLASK_ENV=debug
flask run --reload
```


## Casting Agency Specifications

The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. You are an Executive Producer within the company and are creating a system to simplify and streamline your process.

## Models

Movies with attributes contain title, year, director and genre
Actors with attributes name, role and gender

## Environment Variables

In the User Role
- CASTING_ASSISTANT
- CASTING_DIRECTOR
- EXECUTIVE_PRODUCER

## Roles

Casting Assistant

- GET:actors
- GET:movies

Casting Director
#####  All permissions a Casting Assistant has
- POST:actor
- DELETE:actor
- PATCH:actor
- PATCH:movie

Executive Producer

##### All permissions a Casting Director has
- POST:movie
- DELETE:movie

#### the endpoints of the app 
GET '/actors'
    This endpoint fetches all the actors in the databse and displays them as json 


GET '/movies'
    This endpoint fetches all the movies in the database and displays them as json 

POST '/actors/create'
    This endpoint will create a new actor in the database based on the json that is in the body of the request 


POST '/movies/create'
    This endpoint will create a new movie in the database based on the json that is in the body of the request 

DELETE '/actors/delete/int:actor_id'
    This endpoint will delete the actor that corresponds to the actor ID that is passed into the url 

DELETE '/movies/delete/int:movie_id'
    This endpoint will delete the movie that corresponds to the movie ID that is passed into the url 


PATCH '/actors/edit/int:actor_id' 
    This endpoint will modify the actor that corresponds to the actor ID that is passed into the url based on the json that is passed into the body of the request 

PATCH '/movies/edit/int:movie_id'
    This endpoint will modify the movie that corresponds to the movie ID that is passed into the url based on the json that is passed into the body of the request
