# TODO

from cs50 import get_string

input = get_string("Number: ")

temp = []
for c in input:
    temp.append(c)

if len(temp) != 13 and len(temp) != 15 and len(temp) != 16 :
    print("INVALID\n")
    quit()

product = 0
for i in range(len(temp), 0, -2):
    r = temp[i] * 2
    product += r % 10
    



