from datetime import datetime
from app import db

class Playlist(db.Model):
    __tablename__ = 'playlists'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    # Define relationship to playlist_songs
    playlist_songs = db.relationship('PlaylistSong', backref='playlist', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'created_at': self.created_at,
            'user_id': self.user_id
        }
