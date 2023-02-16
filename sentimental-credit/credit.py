# TODO

from cs50 import get_string

input = get_string("Number: ")

temp = []
for c in input:
    temp.append(c)

if len(temp) != 13 and len(temp) != 15 and len(temp) != 16 :
    print("INVALID\n")
    quit()

for i in range(0, len(temp), 2):
    
