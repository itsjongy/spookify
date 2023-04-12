from datetime import datetime

from . import db

class Playlist(db.Model):
    __tablename__ = 'playlists'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    image_url = db.Column(db.String(255), nullable=False, default='https://community.spotify.com/t5/image/serverpage/image-id/55829iC2AD64ADB887E2A5/image-size/large?v=v2&px=999')

    # Define relationship to playlist_songs
    playlist_songs = db.relationship('PlaylistSong', backref='playlist', lazy=True)

    def __init__(self, title, user, image_url=None):
        self.title = title
        self.user = user
        self.image_url = image_url

    def can_be_modified_by(self, user):
        return self.user == user

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'created_at': self.created_at,
            'user_id': self.user_id,
            'image_url': self.image_url
        }
