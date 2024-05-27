# route.py
from flask import Blueprint, render_template, redirect, url_for
from .utils import generate_breadcrumbs  # 假设这个函数在utils.py中
from flask import flash
from flask_login import login_user, logout_user, login_required


bp = Blueprint('main', __name__)


@bp.route('/')
def home():
    breadcrumbs = [{'name': 'Home'}]  # 面包屑列表，初始为首页
    return render_template('index.html', breadcrumbs=breadcrumbs)


@bp.route('/about')
def about():
    return render_template('About.html')


@bp.route('/category/<category_name>')
def category(category_name):
    breadcrumbs = generate_breadcrumbs(category_name)  # 调用生成面包屑导航的函数
    return render_template('category.html', category_name=category_name, breadcrumbs=breadcrumbs)
