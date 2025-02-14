from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

# Initialisierung der Datenbank und des Loginmanagers
db = SQLAlchemy()
login_manager = LoginManager()

# Erstellung der Flask-App
def create_app():
    app = Flask(__name__)
# Konfiguration der Anwendung
# SECRET_KEY ist ein Schlüssel, der für die Verschlüsselung von Daten in der Anwendung verwendet wird.
    app.config['SECRET_KEY'] = 'your_default_secret_key'  
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'  
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Initialisierung der Datenbank und des Loginmanagers
    db.init_app(app)
    migrate = Migrate(app, db)
    login_manager.init_app(app)
    login_manager.login_view = 'main.login' 
# Laden des Benutzers für Flask-Login

    from .models import User
# Die load_user-Funktion wird von Flask-Login verwendet, um den Benutzer anhand seiner ID zu laden.

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
# Registrierung des Blueprint für die Hauptrouten der Anwendung

    from .routes import main_blueprint 
    app.register_blueprint(main_blueprint)
# Erstellung der Datenbanktabellen

    with app.app_context():
        db.create_all()

    return app