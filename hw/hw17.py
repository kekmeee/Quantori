from exif import Image
from hw16 import gps_location_view
import os


def dms_coor_to_dd_coors(coordinates, coordinates_ref):
    decimal_degrees = coordinates[0] + \
                      coordinates[1] / 60 + \
                      coordinates[2] / 3600
    if coordinates_ref == "S" or coordinates_ref == "W":
        decimal_degrees = -decimal_degrees
    return decimal_degrees


imgdir = "tmp/img/"

for img in os.listdir(imgdir):
    with open(imgdir + img, "rb") as palm_1_file:
        palm_1_image = Image(palm_1_file)
        images = [palm_1_image]
    for index, image in enumerate(images):
        lat = str(dms_coor_to_dd_coors(image.gps_latitude, image.gps_latitude_ref))
        lon = str(dms_coor_to_dd_coors(image.gps_longitude, image.gps_longitude_ref))
        gps_location_view(lat, lon)
