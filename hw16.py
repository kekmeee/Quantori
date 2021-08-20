from hw16_function import gps_location_view

with open("tmp/input.txt", "r") as inp:
    for i in inp:
        lat = ''.join(i.split(";")[0])
        lon = ''.join(i.split(";")[-1][:-1])
        gps_location_view(lat, lon)
inp.close()
