from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email
from wtforms.fields.html5 import EmailField

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

app.config['SECRET_KEY'] = 'POGCHAMPS_ONLY'

class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    email = EmailField('What is your UofT Email Address?', validators=[DataRequired(), Email()])
    submit = SubmitField('Submit')

@app.route('/', methods=['Get', 'Post'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        old_email = session.get('email')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        if old_name is not None and old_email != form.email.data:
            flash('Looks like you have changed your email')
        session['name'] = form.name.data
        session['email'] = form.email.data
        return redirect(url_for('index'))
    return render_template('index.html', form = form, name = session.get('name'), email = session.get('email'))
@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)

#Note: Used https://stackoverflow.com/questions/25324113/email-validation-from-wtform-using-flask to help get the email stuff for part 4
