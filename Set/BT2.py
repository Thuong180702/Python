def reverse_unique_elements(input_set):
    unique_elements_list = list(input_set)
    
    unique_elements_list.reverse()
    
    reversed_set = set(unique_elements_list)
    
    return reversed_set

original_set = {5, 2, 8, 2, 1, 5}
result = reverse_unique_elements(original_set)
print(result)