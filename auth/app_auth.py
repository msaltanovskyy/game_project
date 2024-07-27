import datetime
from flask import Flask, render_template, redirect, url_for, request, flash,session
from context import database as cx
from werkzeug.security import generate_password_hash, check_password_hash
from utils import generate_token #создание токена
from markupsafe import escape #экранирование запроса

app = Flask("auth", template_folder="templates")
app.secret_key = "123"


@app.route('/')
def index():
    if 'login' in session:
        token = generate_token(session['login'])
        return redirect(f'http://127.0.0.1:5002/?user_info={token}')
    return redirect('/auth')


@app.route('/auth', methods=['GET', 'POST'])
def auth():
    if request.method == 'POST':
        login = request.form['login']
        password = request.form['password']
        remember = 'remember' in request.form
        user = cx.collections.find_one({"login": escape(login)})
        if user and check_password_hash(user['password'], password):
            session['login'] = login
            token = generate_token(login)
            flash('Login Successful!', 'success')
            response = redirect(f'http://127.0.0.1:5002/?user_info={token}')
            if remember:
                session.permanent = True
                app.permanent_session_lifetime = datetime.timedelta(days=30)
            return response
        else:
            flash("Wrong login or password!", 'danger')
            return redirect(url_for('auth'))
    return render_template('auth.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nick = request.form['nick']
        login = request.form['login']
        password = request.form['password']
        hash_password = generate_password_hash(password)
        if cx.collections.find_one({"login": escape(login)}) is None:
            user = {
                "nick": nick,
                "login": login,
                "password": hash_password,
            }
            cx.collections.insert_one(user)
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('auth'))
        else:
            flash('Email already registered', 'danger')
    return render_template("register.html")


@app.route('/restore_password', methods=['GET', 'POST'])
def restore_password():
    if request.method == 'POST':
        login = request.form['login']
        user = cx.collections.find_one({"login": escape(login)})
        if user:

            flash('Password reset instructions have been sent to your email.', 'success')
        else:
            flash('Email not found.', 'danger')
        return redirect(url_for('restore_password'))
    return render_template('restore_password.html')


@app.route('/logout')
def logout():
    session.pop('login', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('auth'))


if __name__ == '__main__':
    app.run(port=5001, debug=True)
