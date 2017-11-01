from geopy.geocoders import Nominatim


def cal_lon_lat(sour, recursion=0):
	geolocator = Nominatim()
	try:
		location = geolocator.geocode(sour)
	except GeocoderTimedOut as e:
		if recursion > 20:
			raise e	
	info = (location.latitude, location.longitude)
	return info[0], info[1]


