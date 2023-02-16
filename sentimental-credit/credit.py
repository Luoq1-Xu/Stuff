# TODO

from cs50 import get_string
from math import trunc

input = get_string("Number: ")

# Read string input into a list of ints
temp = []
for c in input:
    temp.append(int(c))

y = len(temp)
if y != 13 and y != 15 and y != 16:
    print("INVALID\n")
    quit()

# Summing the digits of the product of the things that need to be muliplied
product = 0
for i in range(y - 2, -1, -2):
    r = temp[i] * 2
    product += r % 10
    product += trunc(r / 10)

# Summing the remaining digits
for i in range(y - 1, -1, -2):
    product += temp[i]

# Is the Checksum legit
if (product % 10) == 0:
    legit = 1
else:
    print("INVALID\n")
    quit()

# x denotes the first two digits as an integer (for ease of comparison)
x = (temp[0] * 10) + temp[1]


if legit == 1 and y == 15 and (x == 34 or x == 37):
    print("AMEX\n")
elif legit == 1 and y == 16 and (x > 50 and x < 56):
    print("MASTERCARD\n")
elif legit == 1 and (y == 13 or y == 16) and temp[0] == 4:
    print("VISA\n")
else:
    print("INVALID\n")

quit()

