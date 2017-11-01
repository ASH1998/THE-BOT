from math import cos, asin, sqrt
from lat_lon import cal_lon_lat

dst = {'Distance':''}

def distance(origin, destination):
    lat1, lon1 = cal_lon_lat(origin)
    lat2, lon2 = cal_lon_lat(destination)
    radius = 6371 # km

    dlat = math.radians(lat2-lat1)
    dlon = math.radians(lon2-lon1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = radius * c
    dst['Distance'] = round(d, 2)
    return dst

def distance1(origin, destination):
    lon1, lat1 = cal_lon_lat(origin)
    lon2, lat2 = cal_lon_lat(destination)
    p = 0.017453292519943295     #Pi/180
    a = 0.5 - cos((lat2 - lat1) * p)/2 + cos(lat1 * p) * cos(lat2 * p) * (1 - cos((lon2 - lon1) * p)) / 2
    return 12742 * asin(sqrt(a)) #2*R*asin..





if __name__ == '__main__':
	print distance1('dehli', 'Bangalore')