from flask import Flask, render_template, redirect, url_for, request
from Forms import *

app = Flask(__name__)


@app.route('/')
def login():
    login_form = LoginForm(request.form)
    if request.method == 'POST':
        return render_template('login.html', form=login_form)
    else:
        return render_template('login.html', form=login_form)


@app.route('/register')
def register():
    return render_template('login.html')


@app.route('/home')
def home():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
