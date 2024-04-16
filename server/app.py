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

class Playlists(Resource):
    def get(self):
        playlists = [playlist.to_dict() for playlist in Playlist.query.all()]
        return make_response(playlists, 200)        
    
    def post(self):
        request_json = request.get_json()

        name = request_json.get('name')

        new_playlist = Playlist(
            name=name,
            user_id=session['user_id'],
        )
        try:
            db.session.add(new_playlist)
            db.session.commit()
            return new_playlist.to_dict(), 201
        
        except IntegrityError:
            return {'error': '422 Unprocessable Entity'}, 422

class PlaylistByID(Resource):
    def get(self, id):
        playlist = Playlist.query.filter_by(id=id).first().to_dict()
        return make_response(playlist, 200)
    
    def patch(self, id):
        playlist = Playlist.query.filter_by(id=id).first()

        request_json = request.get_json()

        for attr in request_json:
            setattr(playlist, attr, request_json[attr])

        db.session.add(playlist)
        db.session.commit()

        return make_response(playlist.to_dict(), 200)