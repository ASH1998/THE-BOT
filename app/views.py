from flask import Flask
from flask_restful import Resource, Api
from app.modules.map_distance.dist import distance 



app = Flask(__name__)
api = Api(app)



class Dist(Resource):
    def get(self, key ,source, dest):
    	if key == 'd':
    		return distance(source, dest)

api.add_resource(Dist, '/<string:key>/<string:source>/<string:dest>')

if __name__ == '__main__':
    app.run(debug=True)