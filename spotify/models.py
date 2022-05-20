from flask_sqlalchemy import SQLAlchemy

# creating the database and connecting to it.
DB = SQLAlchemy()

class Song(DB.Model):
    id = DB.Column(DB.BigInteger, primary_key=True, nullable=False)
    title = DB.Column(DB.String, nullable=False)
    artists = DB.Column(DB.String, nullable=False)

    def __repr__(self):
        return f'<Song title: {self.title}>'

