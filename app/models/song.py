from app import db
from datetime import datetime

class Song(db.Model):
    __tablename__ = "songs"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    artist_name = db.Column(db.String(100), nullable=False)
    album_name = db.Column(db.String(100), nullable=False)
    release_date = db.Column(db.Date, nullable=False)
    cover_photo = db.Column(db.String(255), nullable=False, default='https://community.spotify.com/t5/image/serverpage/image-id/55829iC2AD64ADB887E2A5/image-size/large?v=v2&px=999')
    audio_file = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "artist_name": self.artist_name,
            "album_name": self.album_name,
            "release_date": self.release_date.strftime("%Y-%m-%d"),
            "cover_photo": base64.b64encode(self.cover_photo).decode('utf-8') if self.cover_photo else None,
            "audio_file": self.audio_file,
        }
