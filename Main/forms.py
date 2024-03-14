from tkinter.ttk import Style
from turtle import color
from flask_wtf import FlaskForm
from wtforms.fields import SubmitField, StringField
from wtforms.validators import InputRequired, email

# form used in cart
class CheckoutForm(FlaskForm):
    firstname = StringField("First Name", validators=[InputRequired()])
    surname = StringField("Surname", validators=[InputRequired()])
    email = StringField("Email", validators=[InputRequired(), email()])
    phone = StringField("Phone Number", validators=[InputRequired()])
    address = StringField("Address", validators=[InputRequired()])
    submit = SubmitField("Complete Order")



