def sort_strings_by_second_character(input_list):
    return sorted(input_list, key=lambda s: s[1])


input_list = ["apple", "banana", "cherry", "date", "fig"]
result_list = sort_strings_by_second_character(input_list)
print(result_list)
