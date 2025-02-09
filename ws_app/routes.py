from flask import Blueprint, render_template, redirect, url_for, request, jsonify, flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User, db, Workspace, Note
from .forms import CreateWorkspaceForm

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
    workspaces = Workspace.query.filter_by(owner_id=current_user.id).all()
    shared_workspaces = Workspace.query.join(Note).filter(Note.user_id == current_user.id).all()
    return render_template(
        'dashboard.html',
        user=current_user,
        workspaces=workspaces,
        shared_workspaces=shared_workspaces
    )

@main_blueprint.route('/workspace/create', methods=['GET', 'POST'])
@login_required
def create_workspace():
    form = CreateWorkspaceForm()
    if form.validate_on_submit():
        new_workspace = Workspace(
            name=form.name.data,
            owner_id=current_user.id,
            privacy=form.privacy.data
        )
        db.session.add(new_workspace)
        db.session.commit()
        flash('Workspace created successfully!', 'success')
        return redirect(url_for('main.dashboard'))
    return render_template('create_workspace.html', form=form)

@main_blueprint.route('/settings')
@login_required
def settings():
    return render_template('settings.html', user=current_user)

@main_blueprint.route('/update_user', methods=['POST'])
@login_required
def update_user():
    new_username = request.form.get('username').strip()
    new_password = request.form.get('password').strip()
    confirm_password = request.form.get('confirm_password').strip()

    if not new_username and not new_password:
        flash('Bitte gib mindestens einen neuen Benutzernamen oder ein neues Passwort ein.', 'error')
        return redirect(url_for('main.settings'))

    if new_password and not confirm_password:
        flash('Bitte bestätige dein neues Passwort.', 'error')
        return redirect(url_for('main.settings'))

    if new_password and (new_password != confirm_password):
        flash('Die eingegebenen Passwörter stimmen nicht überein.', 'error')
        return redirect(url_for('main.settings'))

    if new_username and not new_password:
        current_user.username = new_username
        db.session.commit()
        flash('Dein Benutzername wurde erfolgreich aktualisiert.', 'success')
        return redirect(url_for('main.settings'))

    if new_password and not new_username:
        current_user.set_password(new_password)
        db.session.commit()
        flash('Dein Passwort wurde erfolgreich aktualisiert. Bitte logge dich erneut ein.', 'success')
        logout_user()
        return redirect(url_for('main.login'))

    if new_username and new_password:
        current_user.username = new_username
        current_user.set_password(new_password)
        db.session.commit()
        flash('Deine Daten wurden erfolgreich aktualisiert. Bitte logge dich erneut ein.', 'success')
        logout_user()
        return redirect(url_for('main.login'))

@main_blueprint.route('/delete_account', methods=['GET'])
@login_required
def delete_account():
    user = User.query.get(current_user.id)

    Workspace.query.filter_by(owner_id=current_user.id).delete()
    Note.query.filter_by(user_id=current_user.id).delete()
    
    db.session.delete(user)
    db.session.commit()

    flash("Dein Account wurde erfolgreich gelöscht.", "info")
    return redirect(url_for('main.index'))

@main_blueprint.route('/demo')
def demo():
    return render_template('dummy_page.html')

@main_blueprint.route('/api/workspaces', methods=['GET'])
@login_required
def get_workspaces():
    workspaces = Workspace.query.filter_by(owner_id=current_user.id).all()
    shared_workspaces = Workspace.query.join(Note).filter(Note.user_id == current_user.id).all()
    return jsonify({
        'owned_workspaces': [{'id': w.id, 'name': w.name, 'privacy': w.privacy} for w in workspaces],
        'shared_workspaces': [{'id': w.id, 'name': w.name, 'owner_id': w.owner_id} for w in shared_workspaces]
    })

@main_blueprint.route('/api/workspaces', methods=['POST'])
@login_required
def create_workspace_api():
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