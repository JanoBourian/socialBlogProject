from flask import Flask
from flask import make_response
from flask import render_template
from flask import session
from flask import redirect
from flask import url_for
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from datetime import datetime

app = Flask(__name__)
moment = Moment(app)
app.config["SECRET_KEY"] = "hard to guess string"


class NameForm(FlaskForm):
    name = StringField("What is your name?", validators=[DataRequired()])
    submit = SubmitField("Submit")


@app.route("/", methods=["GET", "POST"])
def index():
    form = NameForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        return redirect(url_for('index'))
    response = make_response(
        render_template(
            "index.html", current_time=datetime.utcnow(), form=form, name=session.get("name", "")
        ),
        200,
    )
    return response


@app.route("/username/<name>")
def user(name: str):
    return render_template("user.html", name=name), 200


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"), 500
