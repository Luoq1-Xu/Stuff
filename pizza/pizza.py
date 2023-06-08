import sys

argc = len(sys.argv)
if argc < 2:
    sys.exit("Too few command-line arguments")
elif argc > 2:
    sys.exit("Too many command-line arguments")

test = sys.argv[1].split(".")
if test[1] != "csv":
    sys.exit("Not a CSV file")
