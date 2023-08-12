# -*- encoding: utf-8 -*-

"""
API Endpoint Initialization and Defination Section

.. versionchanged: 
The `app` and `api` endpoints are defined under app-level, such that
both the `manage.py` and `test` engine can access the same API, thus
all the endpoints can now be defined at one point and can be accessed
from the total module.
"""

import os

from flask_restful import Api
from flask import send_from_directory

from app.main import create_app # controlling application

# * define `APP_ROOT_DIR` & `PROJECT_ROOT_DIR` - for global usage
APP_ROOT_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)))
PROJECT_ROOT_DIR = os.path.join(APP_ROOT_DIR, "..") # `manage.py` file location

# define api version, is also sent for identification
__version__ = open(os.path.join(APP_ROOT_DIR, "VERSION"), "r").read()

# define project type from `config.py` or `.env` file or `$PATH`
# configure different environment under `PROJECT_ENV_NAME` like:
#   > `test`  : run `unittest` for code checking and compatibility
#   > `debug` : run the project under degubbing mode, and for testing
PROJECT_ENVIRON = os.getenv("PROJECT_ENV_NAME") or "dev"
app = create_app(PROJECT_ENVIRON) # check config.py

# adding favicon to flask-docker-template
# all application does have a favicon, and flask_restful
# also supports adding an favicon
# https://flask.palletsprojects.com/en/2.0.x/patterns/favicon/
# https://stackoverflow.com/a/48386934/6623589
# However, in most RESTFUL Design, favicon might be unnecessary
# but, if not defined the following error is raised:
# <host> - - [<date time>] "←[33mGET /favicon.ico HTTP/1.1←[0m" 404 -
# favicon.jpeg is collected from https://icon-library.com/icon/icon-www-6.html
# JPEG file is present in static and ico file is generated using https://icoconvert.com/
@app.route('/favicon.ico')
def favicon():
    # use os.path.join() syntax if not using static directory
    # like os.path.join(".", "static")
    __ICO_PATH__ = os.path.join(PROJECT_ROOT_DIR, "assets", "logo", "favicon.ico")
    return send_from_directory(__ICO_PATH__, mimetype = "image/vnd.microsoft.icon", path = __ICO_PATH__)

# create `api` object using `Api` and define all endpoints
# .. versionchanged:
# Starting this version, all projects are defined with a prefix,
# just to identify the type of project the code is running on. This
# can be adjusted or removed if need be.
if PROJECT_ENVIRON == "test":
    prefix = "/testing"
elif PROJECT_ENVIRON == "dev":
    prefix = "/dev"
else:
    prefix = f"/api/{PROJECT_ENVIRON}/"

api = Api(app, prefix = prefix)

### --- List of all Resources --- ###
from app.main.application.api import * # noqa: F401, F403
from app.main.application.controller import * # noqa: F401, F403

### --- List of all Added Resources to API --- ###
api.add_resource(HelloWorld, "/hello", endpoint = "hello")
