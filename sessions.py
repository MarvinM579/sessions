from flask import Flask, render_template, redirect, request, session
import mysql.connector


app = Flask('MyApp')

conn = mysql.connector.connect(
    user='root',
    password='',
    host='127.0.0.1',
    database='Randoms')

cur = conn.cursor()


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/login', methods=['GET'])
def login():
    return render_template("login.html")


@app.route('/submit_login', methods=['POST'])
def submit_login():
    username = request.form.get('username')
    password = request.form.get('password')
    query = ("SELECT * FROM tbl_user WHERE user_username = '%s'" % username)
    cur.execute(query)
    if password == 'user_password':
        session['username'] = username
    else:
        return redirect('/login')
    return redirect('/')

app.secret_key = 'hello happy kitty'

if __name__ == '__main__':
    app.run(debug=True)
