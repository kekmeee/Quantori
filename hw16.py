from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="Mozilla/5.0 (X11; Linux i686; rv:2.0.1) Gecko/20100101 Firefox/4.0.1")

with open("input.txt", "r") as inp:
    for i in inp:
        lat = ''.join(i.split(";")[0])
        lon = ''.join(i.split(";")[-1][:-1])
        location = geolocator.reverse(str(lat + "," + lon), timeout=10, language="es")
        print(f"Input data:\n{lat};{lon}")
        print(f"Output data:\nLocation: {location.address}\n"
              f"Goggle Maps URL: https://www.google.com/maps/search/?api=1&query={lat},{lon}\n\n")
inp.close()
