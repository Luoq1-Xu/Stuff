import sys
from PIL import Image
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
    ...

except FileNotFoundError:
    sys.exit=()