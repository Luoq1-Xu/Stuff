# TODO
from cs50 import get_int

while True:
    rows = get_int("Height: ")
    if rows > 0 and rows < 9:
        break

for counter in range(1, rows + 1):
    print((" " * (rows - counter)) + ("#" * counter) + "  " + ("#" * counter))


quit()