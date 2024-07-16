from flask import Flask, render_template,redirect,url_for, request


app = Flask("auth",template_folder = "templates")


@app.route('/')
def index():
    return redirect('/auth')


@app.route('/auth', methods=['GET', 'POST'])
def auth():
    if request.method == 'POST':
        login = request.form['login']
        password = request.form['password']
        return redirect(url_for('auth'))
    return render_template('auth.html')


if __name__ == '__main__':
   app.run()
   app.run(debug=True)