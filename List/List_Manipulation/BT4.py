def find_common_elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    common_elements = list(set1.intersection(set2))
    return common_elements


list1 = [1, 2, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 6, 7]
common_elements_list = find_common_elements(list1, list2)
print(common_elements_list)
