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

@app_views.route('/status')
@app_views.route('/status/')
def status():
    return jsonify({"status": "OK"})


@app_views.route('/stats')
@app_views.route('/stats/')
def stats():
    classess = {"users": User,"amenities": Amenity, "cities": City,"places": Place, "reviews": Review, "states": State}
    s = {}
    for c in classess.keys():
        s[c] = storage.count(classess[c])
        
    return jsonify(s)
