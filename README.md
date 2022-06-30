# socialBlogProject
A social blog with Flask. This project was built like a learn tool.

# Index

* [All imports that you need](#section1)
* [All packages](#section2)
* [Start app](#section3)
* [About Flask](#section4)
    * [Flask context](#section4-1)
    * [Request Object](#section4-2)
    * [Request Hooks](#section4-3)
    * [Response Object](#section4-4)
* [Templates](#section5)
    * [Jinja2 filters](#section5-1)
    * [Control Structures](#section5-2)
    * [Flask Bootstrap](#section5-3)
    * [Links](#section5-4)
    * [Static Files](#section5-5)
    * [Time and Flask Moment](#section5-6)
* [Web Forms](#section6)
    * [Configuration](#section6-1)
    * [Form Classes](#section6-2)
    * [HTML Rendering of Forms](#section6-3)
    * [Form Handling in view functions](#section6-4)
    * [Redirects and User Sessions](#section6-5)
    * [Message Flashing](#section6-6)
* [Databases](#section7)
* [Email](#section8)
* [Large Application Structure](#section9)

<div id="section1"></div>

# All imports that you need

```python
from flask import Flask
from flask import request
from flask import make_request
from flask import redirect
from flask import abort
from flask import render_template
from flask_bootstrap import Boostrap
from flask_moment import Moment
from datetime import datetime
```

<div id="section2"></div>

# All packages

```bash
black
flask
flask-bootstrap
flask-moment
```

<div id="section3"></div>

# Start App

The basic structure

```python
from flask import Flask
from flask import make_response
from flask import render_template

app = Flask(__name__)


@app.route("/")
def index():
    response = make_response("<h1> Hello world </h1>", 200)
    response.set_cookie("answer", "17")
    return response

@app.route("/username/<name>")
def user(name:str):
    return render_template("index.html", name=name), 200

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
```

Starts in console
```batch
set FLASK_APP=app.py
set FLASK_DEBUG=1
flask run --host 0.0.0.0
```

<div id="section4"></div>

# About Flask

<div id="section4-1"></div>

## The Flask context

* app context
    * current_app
    * g
* request context
    * request
    * session

<div id="section4-2"></div>

## The request object

* form
* args
* values
* cookies
* headers
* files
* get_data()
* get_json()
* blueprint
* endpoint
* method
* scheme
* is_secure()
* host
* path
* query_string
* full_path
* url
* base_url
* remote_addr
* environ

<div id="section4-3"></div>

## The request hooks

Flask gives you the option to register common functions to be invoked before or after a request is dispatched:

* before_request
* before_first_request
* after_request
* teardown_request

<div id="section4-4"></div>

## The response object

* status_code
* headers
* set_cookie()
* delete_cookie()
* contect_length
* content_type
* set_data()
* get_data()

<div id="section5"></div>

# Templates

Templates resolves the mix of _business logic_ and _presentation logic_

<div id="section5-1"></div>

## Jinja filters

* safe
* capitalize
* lower
* upper
* title
* trim
* striptags

<div id="section5-2"></div>

## Control structures

* if
```html
{% if user %}
    Hello {{user}}
{% else %}
    Hello, stranger!
{% endif %}
```

* for
```html
<ul>
    {% for comment in comments %}
        <li> {{comment}} </li>
    {% endfor %}
</ul>
```

* macros
```html
{% macro render_comment(comment%}
    <li> {{comment}} </li>
{% endmacro %}

<ul>
    {% for comment in comments %}
        {{render_comment(comment)}}
    {% endfor %}
</ul>
```

* imported
```html
{% import 'macros.html' as macros%}

<ul>
    {% for comment in comments %}
        {{macros.render_comment(comment)}}
    {% endfor %}
</ul>
```

* block
```html
{% block head %}
    <title>
        {% block title %}
        {% endblock %} 
        - My application
    </title>
{% endblock %}
```

* extends
```html
{% block head %}
    <title>
        {% block title %}
        {% endblock %} 
        - My application
    </title>
{% endblock %}
```

<div id="section5-3"></div>

## Bootstrap

We don't integrate _flask-bootstrap_ in this app because the _flask-bootstrap_ version is 3.x an old version. We work with 5.0 version.

<div id="section5-4"></div>

## Links

Links only should have the _{{url\_for()}}_ tag.

Links for paths
```python
{{url_for(function_name, **kwargs, _external=True)}}
```

<div id="section5-5"></div>

## Static Files

Links for files
```python
{{url_for(static, filename='')}}
```

<div id="section5-6"></div>

## Time and Flask Moment

In the _base.html_ 
```html
{{ moment.include_moment() }}
```

In the _app.py_ function
```python
render_template("index.html", current_time = datetime.utcnow())
```

Shows the currentime 
```html
    <p> The local date and time is {{moment(current_time).format('LLL')}} </p>
    <p> That was {{moment(current_time).fromNow(refresh = True)}} </p>
```

Some methods of Moment.js availables here
```python
format()
fromNow()
fromTime()
calendar()
valueOf()
unix()
```

<div id="section6"></div>

# Web Forms

<div id="section6-1"></div>

## Configuration

<div id="section6-2"></div>

## Form Classes

<div id="section6-3"></div>

## HTML Rendering of Forms


<div id="section6-4"></div>

## Form Handling in View Functions

<div id="section6-5"></div>

## Redirects and User Sessions

<div id="section6-6"></div>

## Message Flashing

<div id="section7"></div>

# Databases

<div id="section8"></div>

# Email

<div id="section9"></div>

# Large Application Structure

<div id="section10"></div>

# User Authentication

<div id="section11"></div>

# User Roles

<div id="section12"></div>