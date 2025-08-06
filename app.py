from flask import Flask, render_template, session, request, redirect, url_for

app = Flask(__name__)
app.secret_key = "atmkbfj"   

@app.route('/', methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        if username == "Saksham" and password == "123":
            session['username'] = username
            return redirect(url_for('dashboard'))
        else:
            return render_template("login.html", error="Invalid Credentials, Try again!")
        
    return render_template("login.html")


@app.route('/dashboard')
def dashboard():
    if 'username' in  session :
        return render_template('dashboard.html', username = session['username'])
    else:
        return redirect(url_for('login'))


@app.route('/logout', methods=['POST'])
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug = True)