import json

import redis
from flask import Flask, render_template, jsonify


REDIS_KEY = 'containers_data'

app = Flask(__name__)

@app.route('/data')
def get_data():
    r = redis.StrictRedis()

    raw_data = r.get(REDIS_KEY)
    
    if raw_data is None:
        raw_data = b'{}'

    data = json.loads(raw_data.decode())
    
    return jsonify(data)

@app.route('/')
def page():
    return render_template('main.jinja2', servers_count=2)

if __name__ == '__main__':
    app.run()
