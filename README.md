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
* [](#section6)

<div id="section1"></div>

# All imports that you need

```python
from flask import Flask
from flask import request
from flask import make_request
from flask import redirect
from flask import abort
```

<div id="section2"></div>

# All packages

```bash
black
Flask
```

<div id="section3"></div>

# Start App

The basic structure

```python
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1> Hello world </h1>"

@app.route("/username/<name>")
def user(name:str):
    return f"<h1> Hello {name} </h1>"
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