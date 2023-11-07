def reverse_strings(input_list):
    reversed_list = [s[::-1] for s in input_list]
    return reversed_list


input_list = ["apple", "banana", "cherry", "date"]
reversed_list = reverse_strings(input_list)
print(reversed_list)
