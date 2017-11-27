import urllib2, urllib, json
import datetime

return_request= {'name':'THE-BOT','datetime':'','response' : {'location':{}, "wind": {}, "atmosphere": {}, "astronomy": {}}}


baseurl = "https://query.yahooapis.com/v1/public/yql?"




class Yweather_Index(object):
	def __init__(self):
		self.baseurl = baseurl 
		self.yql_query = None

	def get_weather(self, place):

		self.yql_query = "select * from weather.forecast where woeid in (select woeid from geo.places(1) where text='{}')".format(place)
		
		yql_url = self.baseurl + urllib.urlencode({'q':self.yql_query}) + "&format=json"
		result = urllib.urlopen(yql_url).read()
		data = json.loads(result)
		return self.parse_result(data)
	

	def parse_result(self, data):
		return_request['response']['location'] = data["query"]['results']['channel']['location']
		return_request['response']['wind'] = data["query"]['results']['channel']['wind']
		return_request['response']['atmosphere'] = data["query"]['results']['channel']['atmosphere']
		return_request['response']['astronomy'] = data["query"]['results']['channel']['atmosphere']
		return_request['datetime'] = str(datetime.datetime.now())

				
		return return_request


if __name__ == "__main__":
	d = Yweather_Index()
	print (d.get_weather('Hubli'))		