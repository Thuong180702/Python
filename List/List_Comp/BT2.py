original_list = ["apple", "banana", "cherry", "date"]
result_list = [len(s) for s in original_list]
result_list_uppercase = [str(length).upper() for length in result_list]
print(result_list_uppercase)
