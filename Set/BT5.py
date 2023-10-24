def exclusive_elements(set1, set2):
    return set1.symmetric_difference(set2)

set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
print(exclusive_elements(set1, set2))
