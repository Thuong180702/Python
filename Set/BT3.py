def c1k2(set1, set2):
    return  set1.difference(set2)

set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
print(c1k2(set1, set2))