# TODO

from cs50 import get_string

input = get_string("Number: ")

temp = []
for c in input:
    temp.append(c)

if len(temp) != (13,15,16):
    print()
