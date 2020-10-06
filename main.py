from flask import Flask, redirect, url_for, render_template, request, sessionfrom datetime import timedeltaapp = Flask(__name__)app.secret_key = "Your Mom Ugly"app.permanent_session_lifetime = timedelta(days=5)@app.route('/')def home():    return render_template('index.html')@app.route('/login', methods=['GET', 'POST'])def login():    error = None    if request.method == 'POST':        if request.form['username'] != 'admin' or request.form['password'] != 'admin':            error = 'Invalid Credentials. Please try again.'        else:            return redirect(url_for('home'))    return render_template('login.html', error=error)@app.route("/user")def user():    if "user" in session:        user = session['user']        return f"<h1>{user}</h1>"    else:        return redirect(url_for('login'))@app.route("/logout")def logout():    session.pop('user', None)    return redirect(url_for("login"))@app.route("/admin")def admin():    return render_template('admin.html')if __name__ == '__main__':    app.run(debug=True)