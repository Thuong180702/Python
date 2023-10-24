def are_disjoint(set1, set2):
    return set1.isdisjoint(set2)

set_a = {1, 2, 3}
set_b = {4, 5, 6}
set_c = {3, 4, 5}

print(are_disjoint(set_a, set_b))
print(are_disjoint(set_a, set_c))
