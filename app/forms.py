from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email
from wtforms import StringField, EmailField, TextAreaField

class ContactForm(FlaskForm):
    name = StringField("Please enter your fullname", validators=[DataRequired()])
    email = EmailField("Please enter your e-mail address", validators=[DataRequired(), Email()])
    subject = StringField("Please enter the subject for your message", validators=[DataRequired()])
    message = TextAreaField("Please enter the message you would like to send", validators=[DataRequired()], render_kw={"rows": "3"})