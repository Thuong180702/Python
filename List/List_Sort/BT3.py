def filter_and_sort_even_numbers(input_list):
    even_numbers = [num for num in input_list if num % 2 == 0]
    sorted_even_numbers = sorted(even_numbers, reverse=True)
    return sorted_even_numbers


input_list = [5, 12, 3, 8, 10, 6, 7, 4]
result_list = filter_and_sort_even_numbers(input_list)
print(result_list)
