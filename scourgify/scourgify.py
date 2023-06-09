import sys


argc = len(sys.argv)
if argc < 3:
    sys.exit("Too few command-line arguments")
elif argc > 3:
    sys.exit("Too few command-line arguments")

list = []
try:
    with open(sys.argv[1], 'r') as readfile:
        for line in readfile:
            linelist = line.split(',')
            list.append(linelist)
            for element in linelist:
                element = element.strip('"')
    with open(sys.argv[2], 'a') as writefile:
        for line in list:
            writefile.append(line)

except NameError:
    sys.exit("Could not read {}".format(sys.argv[2]))