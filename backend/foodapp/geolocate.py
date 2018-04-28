import googlemaps


class GeoLocate:

    def __init__(self, address=None, city=None, country=None):
        self.gmaps = googlemaps.Client(key="AIzaSyC1ullKaTqRdkIy8djqWq7pIkh5A1JaINQ")
        self.geocode = self.geo_locate(address, city, country)

    def geo_locate(self, address, city, country):
        geocode = self.gmaps.geocode(address + ", " + city + ", " + country)
        return geocode[0]["geometry"]["location"]
