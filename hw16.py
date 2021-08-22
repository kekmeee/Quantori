from geopy.geocoders import Nominatim


def gps_location_view(latitude, longitude):
    geolocator = Nominatim(user_agent="Mozilla/5.0 (X11; Linux i686; rv:2.0.1) Gecko/20100101 Firefox/4.0.1")
    location = geolocator.reverse(str(latitude + "," + longitude), timeout=10, language="ru")
    print(f"Input data:\n{latitude};{longitude}\n"
          f"Output data:\nLocation: {location.address}\n"
          f"Goggle Maps URL: https://www.google.com/maps/search/?api=1&query={latitude},{longitude}\n")


if __name__ == "__main__":
    with open("tmp/input.txt", "r") as inp:
        for i in inp:
            lat = ''.join(i.split(";")[0])
            lon = ''.join(i.split(";")[-1][:-1])
            gps_location_view(lat, lon)
    inp.close()
