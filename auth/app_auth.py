from flask import Flask, render_template, redirect, url_for, request, flash
from context import database as cx
app = Flask("auth", template_folder="templates")
app.secret_key = "123"


@app.route('/')
def index():
    return redirect('/auth')


@app.route('/auth', methods=['GET', 'POST'])
def auth():
    if request.method == 'POST':
        login = request.form['login']
        password = request.form['password']
        user = cx.db.find_user_by_login_and_password(login, password)
        if user:
            flash('Login Successful!', 'success')
            return redirect(url_for('auth'))
        else:
            flash("Wrong password!", "danger")
            return redirect(url_for('auth'))
    return render_template('auth.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        login = request.form['login']
        password = request.form['password']
        if cx.db.find_user(login) is None:
            cx.db.add_user(login, password)
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('auth'))
        else:
            flash('Email already registered', 'danger')
    return render_template("register.html")

if __name__ == '__main__':
    app.run(port=5001, debug=True)
