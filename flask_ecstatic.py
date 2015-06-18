"""Serves static files with optional directory index.

Files in static folder are automatically served on static URL by Flask.
See http://flask.pocoo.org/docs/0.10/api/#application-object.

It's recommended to specify static folder and URL path directly on Flask application object,
unless you need additional static folders, or have multiple route handlers for the URL path,
e.g. when serving static files on root URL ('') for any path unmatched with previous routes.
"""

__all__ = 'add handle404'.split()
__version__ = '0.3.0'

import os

from flask import abort, safe_join, send_file, send_from_directory
from functools import wraps

def add(app, url = None, path = None, endpoint=None, decorate=None, index='index.html', **options):
    """Adds static files endpoint with optional directory index."""

    url = url or app.static_url_path or ''
    path = os.path.abspath(path or app.static_folder or '.')
    endpoint = endpoint or 'static_' + os.path.basename(path)
    decorate = decorate or (lambda f: f)
    endpoints = {}

    if path == app.static_folder:
        raise ValueError('Files in `{}` path are already automatically served on `{}` URL by Flask.'
            ' Set Flask app static_folder to None, if you want to serve them using Flask Ecstatic at `{}` URL'
            .format(path, app.static_url_path, url))

    @app.route(url + '/<path:filename>', endpoint = endpoint)
    @handle404
    @decorate
    def static_files(filename):
        if index:
            filename = safe_join(path, filename)
            if os.path.isdir(filename):
                filename = os.path.join(filename, index)
            return send_file(filename, **options)
        else:
            return send_from_directory(path, filename, **options)

    endpoints[endpoint] = static_files

    if index:
         @app.route(url + '/', endpoint = endpoint + '_index')
         @handle404
         @decorate
         def static_index():
             return send_from_directory(path, index, **options)

         endpoints[endpoint + '_index'] = static_index

         if url:
             @app.route(url, endpoint = endpoint + '_index_bare')
             @handle404
             @decorate
             def static_index_bare():
                 return send_from_directory(path, index, **options)

             endpoints[endpoint + '_index_bare'] = static_index_bare

    return endpoints

def handle404(view):
    @wraps(view)
    def decorated_view(**uri_params):
        try:
            return view(**uri_params)
        except IOError:
            abort(404)

    return decorated_view