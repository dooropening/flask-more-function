from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from .mongodb_connect import db
from .models import User


auth = Blueprint('auth', __name__)


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        password_confirm = request.form.get('password_confirm')

        # 检查用户名是否已存在
        existing_user = db.users.find_one({'username': username})
        if existing_user is not None:
            flash('用户名已存在，请选择其他用户名。')
            return redirect(url_for('auth.register'))

        # 检查两次输入的密码是否一致
        if password != password_confirm:
            flash('两次输入的密码不一致。')
            return redirect(url_for('auth.register'))

        # 创建新用户
        hashed_password = generate_password_hash(password)
        db.users.insert_one({'username': username, 'password': hashed_password})

        flash('注册成功，请登录。')
        return redirect(url_for('auth.login'))

    return render_template('register.html')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # 检查用户是否存在
        user = db.users.find_one({'username': username})
        if user and check_password_hash(user['password'], password):
            user_obj = User(user['username'])
            login_user(user_obj)
            return redirect(url_for('main.home'))

        flash('用户名或密码错误。')

    return render_template('login.html')


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))