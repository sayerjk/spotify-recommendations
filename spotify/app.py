from flask import Flask, render_template, request
from .models import DB, Song
from os import getenv

def create_app():

    app = Flask(__name__)

    # Config Vars
    app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    DB.init_app(app)

#  ===================================================================

    @app.route("/")
    def home():
        songs = Song.query.all()
        print(songs, flush=True)
        return render_template('base.html', message='Spotify Recommender', songs=songs)

#  ===================================================================

    @app.route('/reset')
    def reset():
        DB.drop_all()
        DB.create_all()
        # TODO: insert songs into DB
        return "DATABASE HAS BEEN RESET YES!"

#  ===================================================================

    @app.route('/recommend', methods=['POST'])
    def recommend():
        song_title = request.values['song_title']
        print(song_title)

        # Fake Recommended Song Data
        # TODO: Replace this with song recommendations from the ML model
        fake_recommendations = [['Ma Mélodie', 'Feet Peals'],
                                ['Minha Bênção (Ao Vivo)', 'Padre Marcelo Rossi'],
                                ['Stuck In A Glass Elevator', 'The Myriad'],
                                ['Club Hip Hop Beat 2', 'Jorge Quintero'],
                                ['Like...monk-like', 'The Reese Project']]

        return render_template('base.html',
                               message='Spotify Recommender',
                               songs=fake_recommendations)
        

    return app