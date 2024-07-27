from flask import Flask, render_template, request, redirect
from config import auth
app = Flask("game", template_folder="templates")
app.secret_key = "123"


@app.route('/')
def index():
    user_info = request.args.get('user_info')
    if user_info:
        return render_template('index.html', user_info=user_info)
    return render_template('user_not_found.html')


@app.route('/logout', methods=['POST'])
def logout():
    return redirect(f'{auth.protocol}://{auth.ip}:{auth.port}/logout')


@app.route('/start', methods=['GET', 'POST'])
def start():
    return render_template('start')


if __name__ == '__main__':
    app.run(port=5002, debug=True)
