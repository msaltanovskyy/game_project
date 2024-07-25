from flask import Flask, render_template, request

app = Flask("game", template_folder="templates")
app.secret_key = "123"


@app.route('/')
def index():
    user_info = request.args.get('user_info')
    if user_info:
        return render_template('index.html', user_info=user_info)
    return "No user info provided"


if __name__ == '__main__':
    app.run(port=5002, debug=True)
