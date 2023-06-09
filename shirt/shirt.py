import sys
import os
import PIL
from PIL import Image
argc = len(sys.argv)


if argc < 3:
    sys.exit("Too few command-line arguments")
elif argc > 3:
    sys.exit("Too many command-line arguments")

if ((sys.argv[1].split("."))[1] not in ["jpg", "jpeg", "png"]):
    sys.exit("Invalid input")
if ((sys.argv[2].split("."))[1] not in ["jpg", "jpeg", "png"]):
    sys.exit("Invalid output")
if (sys.argv[1].rsplit("."))[1] != (sys.argv[2].rsplit("."))[1]:
    sys.exit("Input and output have different extensions")


try:
    with Image.open(sys.argv[1]) as inputfile:
        inputfilesize = inputfile.size
        with Image.open("shirt.png") as shirt:
            resizedshirt = PIL.ImageOps.fit(shirt, inputfilesize)
        outputimage = inputfile.paste(resizedshirt, resizedshirt)
    outputimage.save(sys.argv[2])
except FileNotFoundError:
    sys.exit("Input does not exist")