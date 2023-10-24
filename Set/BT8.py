def all_elements_even(input_set):
    for element in input_set:
        if element % 2 != 0:
            return False
    return True

input_set1 = {2, 4, 6, 8}
print(all_elements_even(input_set1))
