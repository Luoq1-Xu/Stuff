# TODO

from cs50 import get_string


storage =[]
input = get_string("Text: ")
for c in input:
    storage.append(c)

length = len(storage)
letters = 0
words = 0
sentences = 0

for counter in range(length):

