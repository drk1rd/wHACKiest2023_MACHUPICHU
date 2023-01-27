from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import Form
from wtforms import StringField
from ftod import ftod

app = Flask(__name__)


# Simple form handling using raw HTML forms
@app.route('/', methods=['GET', 'POST'])
def sign_up():
    error = ""
    if request.method == 'POST':
        # Form being submitted; grab data from form.
        first_name = request.form['firstname']
        last_name = request.form['lastname']
        if last_name=='Football':
            ftod(first_name,last_name)
        elif last_name=='Basketball':
            ftod(first_name,last_name)
        elif last_name=='Badminton':
            ftod(first_name,last_name)
        else:
            pass

    # Render the sign-up page
    return render_template('index.html', message=error)

# More powerful approach using WTForms
class RegistrationForm(Form):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')

# Run the application
app.run(debug=True)