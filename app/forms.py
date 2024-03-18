from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SelectField, FileField
from wtforms.validators import InputRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed

class PropertyForm(FlaskForm):
    property_title = StringField('Property Title', validators=[InputRequired()])
    property_description = TextAreaField('Property Description', validators=[InputRequired()])
    num_rooms = IntegerField('No. of Rooms', validators=[InputRequired()])
    num_bathrooms = IntegerField('No. of Bathrooms', validators=[InputRequired()])
    price =  IntegerField('Price', validators=[InputRequired()])
    property_type = SelectField('Property Type', choices=[('House', 'House'), ('Apartment', 'Apartment'), ('Condo', 'Condo')], validators=[InputRequired()])
    location = StringField('Location', validators=[InputRequired()])
    photo = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])



