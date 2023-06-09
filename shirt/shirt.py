import sys
import os
from PIL import Image
from PIL import ImageOps
argc = len(sys.argv)


if argc < 3:
    sys.exit("Too few command-line arguments")
elif argc > 3:
    sys.exit("Too many command-line arguments")


if ((sys.argv[1].rsplit("."))[0] not in ["jpg", "jpeg", "png"]):
    sys.exit("Invalid input")
if ((sys.argv[2].rsplit("."))[0] not in ["jpg", "jpeg", "png"]):
    sys.exit("Invalid output")
if (sys.argv[1].rsplit("."))[0] != (sys.argv[2].rsplit("."))[0]:
    sys.exit("Input and output have different extensions")


try:
    with open(sys.argv[1]) as inputfile:
        inputfilesize = inputfile.size
        with open("shirt.png") as shirt:
            resizedshirt = PIL.ImageOps.fit(shirt, inputfilesize)
        outputimage = inputfile.paste(resizedshirt, resizedshirt)
    outputimage.save(sys.argv[2])
except FileNotFoundError:
    sys.exit=("Invalid output or input")