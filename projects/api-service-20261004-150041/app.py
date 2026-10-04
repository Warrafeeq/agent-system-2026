#!/usr/bin/env python3
"""REST API"""
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy'})

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({'data': [1, 2, 3, 4, 5]})

if __name__ == '__main__':
    app.run(debug=True)
