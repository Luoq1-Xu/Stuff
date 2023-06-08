import sys

argc = len(sys.argv)
if argc < 2:
    sys.exit("Too few command-line arguments")
elif argc > 2:
    sys.exit("Too many command-line arguments")

list = sys.argv[1].split(".")
if list[1] != "py":
    sys.exit("Not a Python file")

number = 0

try:
    with open(sys.argv[1]) as file:
        for line in file:
            remainder = line.strip()
            if remainder[0] != '#' and remainder != '':
                number += 1
except NameError:
    sys.exit("File does not exist")

print('Number of lines: {}'.format(number))