from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if valid_login(request.form['username'], request.form['password']):
            return redirect(url_for('welcome'))
        else:
            error = 'Invalid username/password'
            return render_template('index.html', error=error)
    return render_template('index.html')

def valid_login(username, password):
    return username == 'admin' and password == 'secret'

@app.route('/welcome')
def welcome():
    return 'Welcome, user!'

if __name__ == '__main__':
    app.run()
