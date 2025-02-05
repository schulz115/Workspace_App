from flask import Blueprint, render_template, redirect, url_for

main_blueprint = Blueprint('main', __name__)

@main_blueprint.route('/')
def index():
    return render_template('welcome.html')

@main_blueprint.route('/login')
def login():
    return render_template('login.html')

@main_blueprint.route('/register')
def register():
    return render_template('register.html')
