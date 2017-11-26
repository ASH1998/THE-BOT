from flask import Flask, request,jsonify
import json
from app.modules.map_distance.dist import distance 
from app.modules.weather.get_weather_method import get_the_place
from app.modules.viki.en_wiki import Viki_media as wiki



app = Flask(__name__)




@app.route('/')
def hello():
	return jsonify({'msg':'Hello world'})


@app.route('/api/v1.0/d/<string:source>/<string:dest>')
def dist(source, dest):
		return jsonify(distance(source, dest))


@app.route('/api/v1.0/w/<string:place>')
def Weath(place):
	return get_the_place(place)


@app.route('/api/v1.0/ip')
def ip_y():
	return jsonify({'ip': request.remote_addr}), 200


@app.route('/api/v1.0/wiki/<string:query>')
def vikipdi(query):
	d = wiki()
	return jsonify(d.Viki_page(query))



if __name__ == '__main__':
	app.run(debug=True)