# TODO
from cs50 import get_int

for rows < 1 and rows > 8:
    rows = get_int("Height: ")

for counter in range(rows):
    print((" " * (rows - 1 - counter)) + ("#" * counter) + "  " + ("#" * counter))
