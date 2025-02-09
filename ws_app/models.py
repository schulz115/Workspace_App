from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from . import db  

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def update_user(self, new_username, new_password):
        if new_username:
            self.username = new_username
        if new_password:
            self.set_password(new_password)
        db.session.commit()

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    workspace_id = db.Column(db.Integer, db.ForeignKey('workspace.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('notes', lazy=True))
    workspace = db.relationship('Workspace', backref=db.backref('notes', lazy=True))

class Workspace(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    privacy = db.Column(db.String(10), nullable=False, default='private')
    owner = db.relationship('User', backref=db.backref('workspaces', lazy=True))