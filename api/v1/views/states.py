from api.v1.views import app_views
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from flask import jsonify, abort, make_response, request

@app_views.route('/states')
def st():
    d = storage.all(State)
    print(d)
    for i in d.keys():
        d[i] = d[i].to_dict()
    return jsonify(d)
    

@app_views.route('/states/<string:state_id>',methods=['GET'])
def ss(state_id):
    r=storage.get(State, state_id)
    if r is None:
        abort(404)
    return jsonify(r.to_dict())

@app_views.route('/states/<string:state_id>',methods=['DELETE'])
def dele(state_id):
    st = storage.get(State, state_id)
    if st is None:
        abort(404)
    st.delete()
    storage.save()
    return (jsonify({}))

@app_views.route('/states/', methods=['POST'], strict_slashes=False)
def post_state():
    """create a new state"""
    if not request.get_json():
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    if 'name' not in request.get_json():
        return make_response(jsonify({'error': 'Missing name'}), 400)
    state = State(**request.get_json())
    state.save()
    return make_response(jsonify(state.to_dict()), 201)


@app_views.route('/states/<string:state_id>', methods=['PUT'],
                 strict_slashes=False)
def put_state(state_id):
    """update a state"""
    state = storage.get("State", state_id)
    if state is None:
        abort(404)
    if not request.get_json():
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    for attr, val in request.get_json().items():
        if attr not in ['id', 'created_at', 'updated_at']:
            setattr(state, attr, val)
    state.save()
    return jsonify(state.to_dict())




