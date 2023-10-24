def intersection_of_sets(list_of_sets):
    if not list_of_sets:
        return set()

    result = list_of_sets[0]

    for s in list_of_sets[1:]:
        result = result.intersection(s)

    return result

sets_list = [{1, 2, 3, 4, 5}, {3, 4, 5, 6, 7}, {4, 5, 8}]
result = intersection_of_sets(sets_list)
print(result)
