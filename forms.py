from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField, SelectField, TextAreaField
from wtforms.validators import InputRequired, Length, NumberRange, URL, Optional

class AddPetForm(FlaskForm):
    """Add pet Form"""
    name = StringField('Pet name', validators=[InputRequired()])
    species = SelectField('Spieces', choices=[('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine')])
    photo_url = StringField('Photo URL', validators=[Optional(), URL()])
    age = IntegerField('Age', validators=[Optional(), NumberRange(min=0, max=30)])
    notes = TextAreaField('Notes/Comments', validators=[Optional(), Length(min=10, max=240)])

class EditPetForm(FlaskForm):
    """Edit existing pet"""
    photo_url = StringField('Photo URL', validators=[Optional(), URL()])
    notes = TextAreaField('Notes/Comments', validators=[Optional(), Length(min=10, max=240)])
    available = BooleanField('Avaiable?')