"""Serves static files with optional directory index.

Files in static folder are automatically served on static URL by Flask.
See http://flask.pocoo.org/docs/0.10/api/#application-object.

It's recommended to specify static folder and URL path directly on Flask application object,
unless you need additional static folders, or have multiple route handlers for the URL path,
e.g. when serving static files on root URL ('') for any path unmatched with previous routes.
"""

__all__ = 'add'.split()
__version__ = '0.1.2'

import os

def add(app, url = None, path = None, endpoint=None, decorate=None, index='index.html', send_from_directory=None):
    """Adds static files endpoint with optional directory index."""

    if not send_from_directory:
        from flask import send_from_directory

    url = url or app.static_url_path or ''
    path = os.path.abspath(path or app.static_folder or '.')
    endpoint = endpoint or 'static_' + os.path.basename(path)
    decorate = decorate or (lambda f: f)
    endpoints = {}

    if path == app.static_folder:
        if url != app.static_url_path:
            raise ValueError('Files in `{}` path are automatically served on `{}` URL by Flask.'
                ' Use different path for serving them at `{}` URL'.format(path, app.static_url_path, url))
    else:
         @app.route(url + '/<path:filename>', endpoint = endpoint)
         @decorate
         def static_files(filename):
             return send_from_directory(path, filename)

         endpoints[endpoint] = static_files

    if index:
         @app.route(url + '/', endpoint = endpoint + '_index')
         @decorate
         def static_index():
             return send_from_directory(path, index)

         endpoints[endpoint + '_index'] = static_index

         if url:
             @app.route(url, endpoint = endpoint + '_index_bare')
             @decorate
             def static_index_bare():
                 return send_from_directory(path, index)

             endpoints[endpoint + '_index_bare'] = static_index_bare

    return endpoints