from flask import Blueprint, render_template, redirect, url_for, request, jsonify, flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User, db, Workspace, Note

main_blueprint = Blueprint('main', __name__)

@main_blueprint.route('/')
def index():
    return render_template('welcome.html')

@main_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('main.dashboard'))
        else:
            error = 'Benutzername oder Passwort inkorrekt.'
    return render_template('login.html', error=error)

@main_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        if User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first():
            flash('Username or Email already exists.', 'error')
            return redirect(url_for('main.register'))

        new_user = User(username=username, email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('main.login'))

    return render_template('register.html')

@main_blueprint.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', user=current_user)

@main_blueprint.route('/demo')
def demo():
    return render_template('dummy_page.html')

@main_blueprint.route('/api/workspaces', methods=['GET'])
@login_required
def get_workspaces():
    workspaces = Workspace.query.filter_by(owner_id=current_user.id).all()
    return jsonify([{'id': w.id, 'name': w.name, 'privacy': w.privacy} for w in workspaces])

@main_blueprint.route('/api/workspaces', methods=['POST'])
@login_required
def create_workspace():
    data = request.json
    new_workspace = Workspace(name=data['name'], owner_id=current_user.id, privacy=data.get('privacy', 'private'))
    db.session.add(new_workspace)
    db.session.commit()
    return jsonify({'message': 'Workspace created', 'id': new_workspace.id}), 201

@main_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('main.index'))
