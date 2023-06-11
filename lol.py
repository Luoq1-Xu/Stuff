lst1 = [1, 2, 3, 4]
lst2 = [5, 6, 7, 8]
for i in lst1:
    lst2.append(i)
    lst1.remove(i)
print(lst1)
print(lst2)