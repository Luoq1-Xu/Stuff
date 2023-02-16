# TODO

from cs50 import get_string
from math import trunc

input = get_string("Number: ")

temp = []
for c in input:
    temp.append(int(c))

if len(temp) != 13 and len(temp) != 15 and len(temp) != 16 :
    print("INVALID\n")
    quit()

product = 0
for i in range(len(temp) - 2, 0, -2):
    r = temp[i] * 2
    product += r % 10
    product += trunc(r / 10)

for i in range(len(temp) - 1, 0, -2):
    product += temp[i]

if (product % 10) == 0:
    legit = 1
else:
    print("INVALID\n")
    quit()





