def filter_strings(input_list):
    filtered_list = [s for s in input_list if len(s) > 3 and s[0].lower() in "aeiou"]
    return filtered_list


input_list = ["apple", "banana", "cherry", "date", "fig", "grape"]
filtered_list = filter_strings(input_list)
print(filtered_list)
