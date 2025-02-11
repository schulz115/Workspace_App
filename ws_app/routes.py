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
        username = request.form['username'].strip()
        email = request.form['email'].strip()
        password = request.form['password'].strip()

        existing_user = User.query.filter((User.username == username) | (User.email == email)).first()
        if existing_user:
            flash('Benutzername oder E-Mail ist bereits vergeben.', 'error')
            return redirect(url_for('main.register'))

        new_user = User(username=username, email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        flash('Registrierung erfolgreich! Bitte logge dich ein.', 'success')
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

@main_blueprint.route('/create_workspace', methods=['GET', 'POST'])
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
        flash('Workspace erfolgreich erstellt!', 'success')
        return redirect(url_for('main.dashboard'))
    return render_template('workspace_creation.html', form=form)

@main_blueprint.route('/workspace/<int:id>')
@login_required
def workspace_details(id):
    workspace = Workspace.query.get_or_404(id)
    if workspace.owner_id != current_user.id:
        flash('Du hast keine Berechtigung, diesen Workspace zu sehen.', 'danger')
        return redirect(url_for('main.dashboard'))
    return render_template('workspace_info.html', workspace=workspace)

@main_blueprint.route('/edit_workspace/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_workspace(id):
    workspace = Workspace.query.get_or_404(id)
    if workspace.owner_id != current_user.id:
        flash('Du kannst diesen Workspace nicht bearbeiten.', 'danger')
        return redirect(url_for('main.dashboard'))
    form = CreateWorkspaceForm(obj=workspace)
    if form.validate_on_submit():
        workspace.name = form.name.data
        workspace.privacy = form.privacy.data
        db.session.commit()
        flash('Workspace erfolgreich aktualisiert!', 'success')
        return redirect(url_for('main.dashboard'))
    return render_template('workspace_editing.html', form=form, workspace=workspace)

@main_blueprint.route('/delete_workspace/<int:id>', methods=['POST'])
@login_required
def delete_workspace(id):
    workspace = Workspace.query.get_or_404(id)
    if workspace.owner_id != current_user.id:
        flash('Du kannst diesen Workspace nicht löschen.', 'danger')
        return redirect(url_for('main.dashboard'))
    db.session.delete(workspace)
    db.session.commit()
    flash('Workspace erfolgreich gelöscht.', 'success')
    return redirect(url_for('main.dashboard'))

@main_blueprint.route('/api/create_workspace', methods=['POST'])
@login_required
def api_create_workspace():
    data = request.get_json()
    if not data or 'name' not in data or 'privacy' not in data:
        return jsonify({ "error": "Invalid input" }), 400
    
    new_workspace = Workspace(
        name=data['name'],
        owner_id=current_user.id,
        privacy=data['privacy']
    )
    db.session.add(new_workspace)
    db.session.commit()
    
    return jsonify({ "message": "Workspace created", "workspace": {
        "id": new_workspace.id, "name": new_workspace.name, "privacy": new_workspace.privacy
    }})

@main_blueprint.route('/demo')
def demo():
    return render_template('dummy_page.html')

@main_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Du wurdest ausgeloggt.', 'info')
    return redirect(url_for('main.index'))
