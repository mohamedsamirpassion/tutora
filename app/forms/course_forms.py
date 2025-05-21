from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, TextAreaField, SelectField, FloatField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Optional, NumberRange

class CourseForm(FlaskForm):
    title = StringField('Course Title', validators=[DataRequired(), Length(max=120)])
    description = TextAreaField('Description', validators=[DataRequired()])
    category = SelectField('Category', validators=[DataRequired()],
                          choices=[
                              ('General English', 'General English Program'),
                              ('Conversation', 'Conversation Classes'),
                              ('Phonetics', 'Phonetics and Pronunciation Classes')
                          ])
    image = FileField('Course Image', validators=[
        Optional(),
        FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')
    ])
    duration = StringField('Duration (e.g., "8 weeks")', validators=[DataRequired(), Length(max=64)])
    price = FloatField('Price', validators=[DataRequired(), NumberRange(min=0)])
    is_active = BooleanField('Active')
    submit = SubmitField('Save Course') 