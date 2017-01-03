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


@app.route('/submit_login', methods=['POST', 'GET'])
def submit_login():
    username = request.form.get('username')
    password = request.form.get('password')
    query = ("SELECT * FROM tbl_user WHERE user_password = %s" % username)
    cur.execute(query)
    if user_password == password:
        session['username'] = user_name
        return redirect('/')
    else:
        return redirect('/login')

app.secret_key = 'hello happy kitty'

if __name__ == '__main__':
    app.run(debug=True)
