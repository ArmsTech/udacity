"""Bundled assets used for tech_quote."""

from flask.ext.assets import Bundle

from tech_quote.extensions import assets

CSS = (
    'libs/bootstrap/dist/css/bootstrap.css',)

JS = (
    'libs/jQuery/dist/jquery.js',
    'libs/bootstrap/dist/js/bootstrap.js')

assets.register(
    'css_all', Bundle(*CSS, filters='cssmin', output='gen/packed.css'))
assets.register(
    'js_all', Bundle(*JS, filters='jsmin', output='gen/packed.js'))
