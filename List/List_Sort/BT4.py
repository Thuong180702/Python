def sort_strings_by_length_and_lexicography(input_list):
    return sorted(input_list, key=lambda s: (-len(s), s))


input_list = ["banana", "apple", "date", "grape", "fig", "cherry"]
result_list = sort_strings_by_length_and_lexicography(input_list)
print(result_list)
