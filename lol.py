a = [['a', 'b'], ['c'], 'd']
b = a[:-1]
a[1], b[0][1] = b[0], a[2]
print(a)
print(b)