"""Bundled assets used for tech_quote."""

from flask.ext.assets import Bundle

from tech_quote.extensions import assets

CSS = (
    'libs/bootstrap/dist/css/bootstrap.css',
    'libs/selectize/dist/css/selectize.bootstrap3.css',
    'libs/bootstrap-social/bootstrap-social.css',
    'css/style.css')

JS = (
    'libs/jquery/dist/jquery.js',
    'libs/bootstrap/dist/js/bootstrap.js',
    'libs/selectize/dist/js/standalone/selectize.js',
    'js/app.js')

assets.register(
    'css_all', Bundle(*CSS, filters='cssmin', output='gen/packed.css'))
assets.register(
    'js_all', Bundle(*JS, filters='jsmin', output='gen/packed.js'))
