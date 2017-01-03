from flask import Flask, render_template, redirect, request, session
import pg

db = pg.DB(host="localhost", user="postgres", passwd="rocket", dbname="users")

app = Flask('MyApp')

# loggedIn = False


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
    query = db.query("select * from myuser where username = '%s'" % username)
    result_list = query.namedresult()
    if len(result_list) > 0:
        user = result_list[0]
        if user.password == password:
            session['name'] = user.name
            # loggedIn = True
            return redirect('/')
        else:
            # loggedIn = False
            return redirect('/login')
    else:
        return redirect('/login')


@app.route('/logout', methods=['POST'])
def logout():
    del session['name']
    # loggedIn = False
    return redirect('/')

app.secret_key = 'hello happy kitty'

if __name__ == '__main__':
    app.run(debug=True)
