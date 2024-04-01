from api.v1.views import app_views
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from flask import jsonify

@app_views.route('/status/')
def status():
    return jsonify({"status": "OK"})

@app_views.route('/stats/')
def stats():
    classess = {User: "users",
                        Amenity: "amenities", City: "cities",
                        Place: "places", Review: "reviews",
                        State: "states"}
    s = {}
    for c in classess.keys():
        s[classess[c]] = storage.count(c)
        return jsonify(s)
