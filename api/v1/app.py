#!/usr/bin/python3
"""app"""
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)

@app.teardown_appcontext
def tear(self):
    """Closes the storage engine"""
    storage.close()

@app.errorhandler(404)
def not_found(error):
    """Handles 404 Not Found errors with a custom JSON response"""
    return jsonify({"error": "Not found"}), 404

if __name__ == '__main__':
    from os import getenv
    HBNB_API_HOST = getenv("HBNB_API_HOST", "0.0.0.0")
    HBNB_API_PORT = int(getenv("HBNB_API_PORT", 5000))
    app.run(host=HBNB_API_HOST, port=HBNB_API_PORT, threaded=True)
