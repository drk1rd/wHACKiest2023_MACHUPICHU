from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import Form
from wtforms import StringField
from ftod import ftod
from dtof import dtof
from flask_socketio import SocketIO, send

app = Flask(__name__)


socketio = SocketIO(app, cors_allowed_origins="*")


@socketio.on("message")
def sendMessage(message):
    send(message, broadcast=True)
    # send() function will emit a message vent by default


@app.route("/chat")
def message():
    return render_template("chat.html")


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
            return redirect('/football')
        elif last_name=='Basketball':
            ftod(first_name,last_name)
            return redirect('/basketball')
        elif last_name=='Badminton':
            ftod(first_name,last_name)
            return redirect('/badminton')
        else:
            pass

    # Render the sign-up page
    return render_template('index.html', message=error)

@app.route('/basketball')
def foot():
   bb = dtof("Basketball")
   userl = str(bb).split(',')
   return render_template('basketball.html', userl=userl)



@app.route('/football')
def basket():
   fb=dtof("Football")
   userl = str(fb).split(',')
   return render_template('football.html', userl=userl)

@app.route('/badminton')
def badminton():
   bd=dtof("Badminton")
   userl = str(bd).split(',')
   return render_template('badminton.html', userl=userl)

# Run the application
app.run(debug=True)