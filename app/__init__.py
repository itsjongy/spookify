import os

from flask import Flask, request, session, redirect
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect, generate_csrf
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from config import Config

app = Flask(__name__, static_folder='../react-app/build', static_url_path='/')

app.config.from_object(Config)

# setup application security
CSRFProtect(app)
CORS(app, supports_credentials=True)

# setup database
db = SQLAlchemy(app)
Migrate(app, db)

# setup login manager
login_manager = LoginManager(app)
login_manager.login_view = 'auth.unauthorized'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# enforce https redirect in production
@app.before_request
def https_redirect():
    if os.environ.get('FLASK_DEBUG') != '1' and not request.is_secure:
        url = request.url.replace('http://', 'https://', 1)
        return redirect(url, code=301)

# generate and inject csrf token
@app.after_request
def inject_csrf_token(response):
    csrf_token = generate_csrf()
    response.set_cookie(
        'csrf_token',
        csrf_token,
        secure=request.is_secure,
        samesite='Lax',
        httponly=True)
    return response

# fallback route for React app
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def react_root(path):
    if path == 'favicon.ico':
        return app.send_from_directory('public', 'favicon.ico')
    return app.send_static_file('index.html')
