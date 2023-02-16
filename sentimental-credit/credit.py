# TODO

from cs50 import get_string

input = get_string("Number: ")

list = input.split()
if len(list) != 13 or 15 or 16:
    print("INVALID\n")
    quit()

