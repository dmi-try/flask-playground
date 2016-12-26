# -*- coding: utf-8 -*-

__author__ = """Dmitry Pyzhov"""
__email__ = 'lux.place@gmail.com'
__version__ = '0.0.1'

import urllib2
import json

from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/')
@app.route('/<query>')
def hello(query='world'):
    return render_template('photos.html', query=query)


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='localhost')
