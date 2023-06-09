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
            for element in linelist:
                element = element.replace('\"')
            list.append(linelist)
    with open(sys.argv[2], 'a') as writefile:
        for line in list:
            for element in line:
                writefile.write(element)

except NameError:
    sys.exit("Could not read {}".format(sys.argv[2]))