# TODO

from cs50 import get_string
from math import trunc

input = get_string("Number: ")

temp = []
for c in input:
    temp.append(int(c))

y = len(temp)
if y != 13 and y != 15 and y != 16 :
    print("INVALID\n")
    quit()

product = 0
for i in range(y - 2, 0, -2):
    r = temp[i] * 2
    product += r % 10
    product += trunc(r / 10)

for i in range(y - 1, 0, -2):
    product += temp[i]

if (product % 10) == 0:
    legit = 1
else:
    print("INVALID\n")
    quit()

x = (temp[0] * 10) + temp[1]

if legit == 1 and y == 15 and (x == 34 or x == 37):
    print("AMEX\n")
elif legit == 1 and 



