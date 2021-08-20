from geopy.geocoders import Nominatim


def gps_location_view(latitude, longitude):
    geolocator = Nominatim(user_agent="Mozilla/5.0 (X11; Linux i686; rv:2.0.1) Gecko/20100101 Firefox/4.0.1")
    location = geolocator.reverse(str(latitude + "," + longitude), timeout=10, language="ru")
    print(f"Input data:\n{latitude};{longitude}\n"
          f"Output data:\nLocation: {location.address}\n"
          f"Goggle Maps URL: https://www.google.com/maps/search/?api=1&query={latitude},{longitude}\n")
