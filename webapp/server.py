#!/usr/bin/env python

import simplejson as json
from flask import Flask, jsonify, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html",
                           tiles=range(126))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    
