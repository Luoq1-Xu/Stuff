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
    if storage[counter].isalpha():
        letters += 1
    elif storage[counter] == ' ':
        words += 1
    elif storage[counter] == '.' or storage[counter] == '!' or storage[counter] == '?':
        sentences += 1

words += 1

index = 0.0588 * ((letters/words) * 100) - 0.296 * ((sentences/words) * 100) - 15.8

