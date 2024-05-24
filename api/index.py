from flask import Flask, Blueprint, render_template
from flask_login import LoginManager
from .auth import auth
from .models import User
from .mongodb_connect import db
from .route import bp as main_bp

app = Flask(__name__)
app.secret_key = 'ample_scope'

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)


@login_manager.user_loader
def load_user(username):
    user = db.users.find_one({'username': username})
    if user:
        return User(user['username'])
    return None


app.register_blueprint(main_bp)
app.register_blueprint(auth)
