from ywthr import Yweather_Index





def get_the_place(place):
	d = Yweather_Index()
	return d.get_weather(place)