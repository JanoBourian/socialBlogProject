from flask import Flask
from flask import make_response

app = Flask(__name__)


@app.route("/")
def index():
    response = make_response("<h1> Hello world </h1>", 200)
    response.set_cookie("answer", "17")
    return response

@app.route("/username/<name>")
def user(name:str):
    return f"<h1> Hello {name} </h1>", 200