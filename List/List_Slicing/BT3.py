def remove_first_last_characters(input_list):
    modified_list = [s[1:-1] for s in input_list if len(s) >= 3]
    return modified_list


input_list = ["apple", "banana", "cherry", "date"]
result_list = remove_first_last_characters(input_list)
print(result_list)
