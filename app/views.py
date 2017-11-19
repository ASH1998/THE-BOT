from flask import Flask, request
import json
from flask_restful import Resource, Api
from app.modules.map_distance.dist import distance 
from app.modules.weather.get_weather_method import get_the_place


app = Flask(__name__)
api = Api(app)



class Dist(Resource):
    def get(self, key ,source, dest):
    	if key == 'd':
    		return distance(source, dest)

class Wthr(Resource):
    def get(self, key ,place):
    	if key == 'w':
    		return get_the_place(place)

class Whats_My_ip(Resource):
	def get(self, key):
		return {'ip': request.remote_addr}, 200

api.add_resource(Dist, '/<string:key>/<string:source>/<string:dest>')
api.add_resource(Wthr, '/<string:key>/<string:place>')
api.add_resource(Whats_My_ip, '/<string:key>')


if __name__ == '__main__':
    app.run(debug=True)