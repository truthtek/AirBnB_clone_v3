#!/usr/bin/python3
"""index"""
from api.v1.views import app_views
from flask import jsonify
from models import storage

@app_views.route('/status', methods=['GET'])
def status():
    """Returns the status of the API"""
    return jsonify({'status': 'OK'})

@app_views.route('/stats', methods=['GET'])
def object_stats():
    """Retrieves the number of each object by type"""
    stats = {
        "amenities": storage.count("Amenity"),
        "cities": storage.count("City"),
        "places": storage.count("Place"),
        "reviews": storage.count("Review"),
        "states": storage.count("State"),
        "users": storage.count("User")
    }
    return jsonify(stats)
