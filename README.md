# [Flask-Ecstatic](https://github.com/salsita/flask-ecstatic) <a href='https://github.com/salsita'><img align='right' title='Salsita' src='https://www.google.com/a/cpanel/salsitasoft.com/images/logo.gif?alpha=1' /></a>

Serves static files with optional directory index.

[![Version](https://badge.fury.io/gh/salsita%2Fflask-ecstatic.svg)]
(https://github.com/salsita/flask-ecstatic/tags)
[![PyPI package](https://badge.fury.io/py/Flask-Ecstatic.svg)]
(https://pypi.python.org/pypi/Flask-Ecstatic/)
[![Downloads](https://img.shields.io/pypi/dm/Flask-Ecstatic.svg)]
(https://pypi.python.org/pypi/Flask-Ecstatic/)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/Flask-Ecstatic.svg)]
(https://pypi.python.org/pypi/Flask-Ecstatic/)
[![License](https://img.shields.io/pypi/l/Flask-Ecstatic.svg)]
(https://pypi.python.org/pypi/Flask-Ecstatic/)

Files in static folder are automatically served on static URL by Flask.
See http://flask.pocoo.org/docs/0.10/api/#application-object.

It's recommended to specify static folder and URL path directly on Flask application object,
unless you need additional static folders, or have multiple route handlers for the URL path,
e.g. when serving static files on root URL ('') for any path unmatched with previous routes.


## Supported Platforms

* [Python](http://www.python.org/) >= 2.6, 3.3
* [Flask](http://flask.pocoo.org/) >= 0.9


## Get Started

Install using [pip](https://pip.pypa.io/) or [easy_install](http://pythonhosted.org/setuptools/easy_install.html):
```bash
pip install Flask-Ecstatic
easy_install Flask-Ecstatic
```

## Example:

#### Flask application: `app.py`

```python
#!/usr/bin/env python

"""Flask-based web application."""

__all__ = 'app'.split()

import flask
import flask.ext.ecstatic

app = flask.Flask(__name__, static_folder=None)

# Here initialize your routes, for example an API server on /api/...

# And serve files from `static/` folder for all other URLs.
flask.ext.ecstatic.add(app, '', 'static')

if __name__ == '__main__':
    app.run()
```


## Changelog

### 0.3.0

#### Fixes

- Return 404 for missing or inaccessible files.
- Fix package setup on Python 3.

### 0.2.1

#### Fixes

- Fix package setup to not require dependencies preinstalled.

### 0.2.0

#### Fixes

- Fix serving index file from subdirectories.

### 0.1.2

#### Features

- Add support for endpoint decoration, e.g. with auth.login_required.
- Return map of created endpoints.

### 0.1.1

#### Fixes

- Fix setup without flask installed.

### 0.1.0

#### Features

- Initial release.
