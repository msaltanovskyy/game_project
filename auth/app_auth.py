from flask import Flask, render_template, redirect, url_for, request, flash
from context import database as cx
from utils import check_password, encryption
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
        user = cx.db.find_user(login)
        if user and check_password(password, user['password']):
            flash('Login Successful!', 'success')
            return redirect(url_for('auth'))
        else:
            flash("Wrong login or password!", "danger")
            return redirect(url_for('auth'))
    return render_template('auth.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nick = request.form['nick']
        login = request.form['login']
        password = request.form['password']
        hash_password = encryption(password)  # SHA512
        if cx.db.find_user(login) is None:
            cx.db.add_user(nick, login, hash_password)
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('auth'))
        else:
            flash('Email already registered', 'danger')
    return render_template("register.html")

@app.route('/restore_password', methods=['GET', 'POST'])
def restore_password():
    if request.method == 'POST':
        login = request.form['login']
        user = cx.db.find_user(login)
        if user:
            # Здесь вы можете добавить логику для отправки письма с восстановлением пароля
            flash('Password reset instructions have been sent to your email.', 'success')
        else:
            flash('Email not found.', 'danger')
        return redirect(url_for('restore_password'))
    return render_template('restore_password.html')


if __name__ == '__main__':
    app.run(port=5001, debug=True)
