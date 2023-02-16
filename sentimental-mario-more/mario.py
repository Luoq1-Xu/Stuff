# TODO
from cs50 import get_int

while True:
    rows = get_int("Height: ")
    if rows > 0 and rows < 9:
        break

for counter in range(rows + 1):
    print((" " * (rows - 1 - counter)) + ("#" * counter) + "  " + ("#" * counter))

print()

quit()