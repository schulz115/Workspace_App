from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length

class CreateWorkspaceForm(FlaskForm):
    name = StringField(
        'Workspace Name', 
        validators=[DataRequired(), Length(min=3, max=80)]
    )
    privacy = SelectField(
        'Privacy', 
        choices=[('private', 'Private'), ('public', 'Public')], 
        validators=[DataRequired()]
    )
    submit = SubmitField('Create Workspace')