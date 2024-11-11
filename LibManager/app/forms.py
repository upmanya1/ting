from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField, IntegerField
from wtforms.validators import DataRequired

class StudentForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    contact = StringField('Contact')
    shift_id = IntegerField('Shift ID')
    fees_due = FloatField('Fees Due')
    submit = SubmitField('Save')

class PaymentForm(FlaskForm):
    student_id = IntegerField('Student ID', validators=[DataRequired()])
    amount = FloatField('Amount', validators=[DataRequired()])
    submit = SubmitField('Submit Payment')
