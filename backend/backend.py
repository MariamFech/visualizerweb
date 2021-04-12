#!/usr/bin/env python
# encoding: utf-8
import json
from flask import Flask
from flask import request
from flask_cors import CORS
from algo.compute import compute

app = Flask(__name__)
CORS(app)


@app.route('/compute', methods=['POST'])
def post():
    response = app.response_class(
        response=json.dumps(compute(request.get_json())),
        status=200,
        mimetype='application/json'
    )
    return response


if __name__ == '__main__':
    # app.run(host='0.0.0.0')
    app.run()
