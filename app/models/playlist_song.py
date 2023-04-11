from app import db

class PlaylistSong(db.Model):
    __tablename__ = 'playlist_songs'

    id = db.Column(db.Integer, primary_key=True)
    playlist_id = db.Column(db.Integer, db.ForeignKey('playlists.id'), nullable=False)
    song_id = db.Column(db.Integer, db.ForeignKey('songs.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Define relationship to Playlist
    playlist = db.relationship('Playlist', backref='playlist_songs')

    # Define relationship to Song
    song = db.relationship('Song', backref='playlist_songs')

    # Add ForeignKeyConstraint to ensure referential integrity
    __table_args__ = (
        db.ForeignKeyConstraint(['playlist_id'], ['playlists.id']),
        db.ForeignKeyConstraint(['song_id'], ['songs.id']),
        {'schema': 'public'},
    )

    # Add unique constraint to (playlist_id, song_id) pair
    __table_args__ = (
        db.UniqueConstraint('playlist_id', 'song_id', name='unique_playlist_song'),
        {'schema': 'public'},
    )
