from flask import Flask
from flask import render_template
from api.utils import generate_breadcrumbs  # 导入生成面包屑导航的函数


app = Flask(__name__)


@app.route('/')
def home():
    breadcrumbs = [{'name': 'Home'}]  # 面包屑列表，初始为首页

    return render_template('index.html', breadcrumbs=breadcrumbs)


@app.route('/category/<category_name>')
def category(category_name):
    breadcrumbs = generate_breadcrumbs(category_name)  # 调用生成面包屑导航的函数
    return render_template('category.html', category_name=category_name, breadcrumbs=breadcrumbs)
