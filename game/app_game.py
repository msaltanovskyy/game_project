from flask import Flask, render_template, request, redirect
import config

app = Flask("game", template_folder="templates")
app.config.from_object(config.Config)


@app.route('/')
def index():
    user_info = request.args.get('user_info')
    if user_info:
        return render_template('index.html', user_info=user_info)
    return render_template('user_not_found.html')


@app.route('/logout', methods=['POST'])
def logout():
    return redirect(f'{config.auth.get_url()}/logout')


@app.route('/start', methods=['GET', 'POST'])
def start():
    return render_template('start.html')


if __name__ == '__main__':
    app.run(port=5002, debug=True)
