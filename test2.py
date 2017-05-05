
from pygeocoder import Geocoder
from math import sin, cos, acos, radians

class calcRadiation():

    def init(self,city1,city2):

        city1_loc = self.geocoding(city1)

        city2_loc = self.geocoding(city2)

        distance = self.dist_on_sphere(city1_loc, city2_loc)  # 単位はkm

        if city1_loc[0] < city2_loc[0]:
            speed = 800 # 単位はkm/h
            time = self.calc_flight_time(speed, distance)
            print('{0:.3f}μSv'.format(3.7*0.01*time))
        else:
            speed = 1000  # 単位はkm/h
            time = self.calc_flight_time(speed, distance)

#            print('{0:.3f}μSv'.format(3.7 * 0.01 * time))
	    di = 3.7 * 0.01 * time
            return di

    # 緯度経度を求める
    def geocoding(self,locate):
        results = Geocoder.geocode(locate)
        return results[0].coordinates


    def latlng_to_xyz(self,lat, lng):
        rlat, rlng = radians(lat), radians(lng)
        coslat = cos(rlat)
        return coslat * cos(rlng), coslat * sin(rlng), sin(rlat)

    # 二つの場所の距離を求める
    def dist_on_sphere(self,pos0, pos1, radious=6378.137):
        xyz0, xyz1 = self.latlng_to_xyz(*pos0), self.latlng_to_xyz(*pos1)
        return acos(sum(x * y for x, y in zip(xyz0, xyz1))) * radious

    # 飛行時間を求める
    def calc_flight_time(self,speed, distance):
        time = distance / speed  # 単位はhour
        return float(time)

if __name__ == '__main__':

    # city1,city2に都市名を入力してね
    calcRadiation().init(city1,city2)
