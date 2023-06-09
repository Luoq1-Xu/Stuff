import sys


argc = len(sys.argv)
if argc < 3:
    sys.exit("Too few command-line arguments")
elif argc > 3:
    sys.exit("Too few command-line arguments")

try:
    with open(sys.argv[2]) as readfile:
        for line in readfile:
            
except NameError:
    sys.exit("Could not read {}".format(sys.argv[2]))