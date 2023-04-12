import os

class Config:
    SECRET_KEY = os.environ.get('asdgnaklsdngok12n')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgresql://jason:123@localhost:5432/spookify').replace('postgres://', 'postgresql://', 1)
