import sys
from tabulate import tabulate

argc = len(sys.argv)
if argc < 2:
    sys.exit("Too few command-line arguments")
elif argc > 2:
    sys.exit("Too many command-line arguments")

test = sys.argv[1].split(".")
if test[1] != "csv":
    sys.exit("Not a CSV file")

try:
    with open(sys.argv[1]) as file:
        counter = 0
        header =[]
        table=[]
        for line in file:
            if counter == 0:
                header = (line.rstrip()).split(",")
                counter += 1
            else:
                table.append(line.split(","))
    print(tabulate(table, header, tablefmt="grid"))

except NameError:
    sys.exit("File does not exist")
