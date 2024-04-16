from flask import request, session, make_response
from flask_restful import Api, Resource
from sqlalchemy.exc import IntegrityError

from config import app, db
from models import User, Artist, Playlist, Song

api = Api(app)

@app.route('/')
def index():
    return '<h1>myTunes Back End Development</h1>'

class Users(Resource):
    def get(self):
        users = [user.to_dict() for user in User.query.all()]
        return make_response(users, 200)  

class Music(Resource):
    def get(self):
        music = [artist.to_dict() for artist in Artist.query.all()]
        return make_response(music, 200) 
    
    def post(self):
        request_json = request.get_json()

        name = request_json.get('name')
        spotify_id= request_json.get('spotifyId')
        image_url = request_json.get('imageUrl')
        genres = request_json.get('genres')       
        
        artist = Artist(
            name=name,
            spotify_id=spotify_id,
            image_url=image_url,
            genres=genres,
        )
        
        try:
            db.session.add(artist)
            db.session.commit()
            return {'message' : 'Artist successfully added to database'}, 201
        
        except IntegrityError:
            return {'error': '422 Unprocessable entity'}, 422