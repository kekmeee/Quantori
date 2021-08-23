from glob import glob
from os import path
from PIL import Image

size = (128, 128)

for infile in glob("tmp/img/*.JPG"):
    file, ext = path.splitext(infile)
    with Image.open(infile) as im:
        im.thumbnail(size)
        im.save(file + ".thumbnail", "JPEG")
        print(f"{file + '.thumbnail'} size: {path.getsize(file + '.thumbnail')} byte")