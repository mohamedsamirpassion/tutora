from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length

class BookingForm(FlaskForm):
    booking_date = DateField('Date', format='%Y-%m-%d', validators=[DataRequired()])
    booking_time = SelectField('Time', validators=[DataRequired()], 
                              choices=[
                                  ('09:00 AM', '09:00 AM'),
                                  ('10:00 AM', '10:00 AM'),
                                  ('11:00 AM', '11:00 AM'),
                                  ('12:00 PM', '12:00 PM'),
                                  ('01:00 PM', '01:00 PM'),
                                  ('02:00 PM', '02:00 PM'),
                                  ('03:00 PM', '03:00 PM'),
                                  ('04:00 PM', '04:00 PM'),
                                  ('05:00 PM', '05:00 PM'),
                              ])
    notes = TextAreaField('Notes', validators=[Length(max=500)])
    submit = SubmitField('Book Placement Test')

class AdminBookingForm(FlaskForm):
    status = SelectField('Status', validators=[DataRequired()],
                        choices=[
                            ('pending', 'Pending'),
                            ('confirmed', 'Confirmed'),
                            ('cancelled', 'Cancelled'),
                            ('completed', 'Completed')
                        ])
    notes = TextAreaField('Admin Notes', validators=[Length(max=500)])
    submit = SubmitField('Update Booking') 