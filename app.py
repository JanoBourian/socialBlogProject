from flask import Flask
from flask import make_response
from flask import render_template

app = Flask(__name__)


@app.route("/")
def index():
    response = make_response(render_template("index.html"), 200)
    response.set_cookie("answer", "17")
    return response

@app.route("/username/<name>")
def user(name:str):
    return render_template("user.html", name=name), 200

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500