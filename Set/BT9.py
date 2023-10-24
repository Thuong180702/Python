def no_repeated_elements(input_set):
    return len(input_set) == len(set(input_set))

set1 = {1, 2, 3, 4, 5}
set2 = {1, 2, 2, 3, 4}
print(no_repeated_elements(set1))
print(no_repeated_elements(set2))
