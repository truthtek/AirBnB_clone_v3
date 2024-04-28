from models import storage
from flask import jsonify
from api.v1.views import app_views

@app_views.route('/status', methods=['GET'])
def status():
    return jsonify({"status": "OK"})

@app_views.route('/stats', methods=['GET'])
def object_stats():
    stats = {
        "amenities": storage.count("Amenity"),
        "cities": storage.count("City"),
        "places": storage.count("Place"),
        "reviews": storage.count("Review"),
        "states": storage.count("State"),
        "users": storage.count("User")
    }
    return jsonify(stats)
