def reverse_every_second_element(input_list):
    reversed_second_elements = input_list[1::2][::-1]
    return reversed_second_elements


input_list = [1, 2, 3, 4, 5, 6]
result_list = reverse_every_second_element(input_list)
print(result_list)
