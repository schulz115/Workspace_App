from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length

# Definition des Formulars für die Registrierung
class CreateWorkspaceForm(FlaskForm):
    name = StringField(
        'Workspace Name', 
        validators=[DataRequired(), Length(min=3, max=80)]
    )
    # Definition der Auswahlmöglichkeiten für die Privatsphäre des Workspaces
    privacy = SelectField(
        'Privacy', 
        choices=[('private', 'Private'), ('public', 'Public')], 
        validators=[DataRequired()]
    )
    # Definition des Buttons zum Erstellen des Workspaces
    submit = SubmitField('Create Workspace')