def convert_vowels_to_uppercase(input_list):
    vowels = "aeiouAEIOU"
    modified_list = [
        "".join(c.upper() if c in vowels else c for c in s) for s in input_list
    ]
    return modified_list


input_list = ["apple", "banana", "cherry", "date"]
result_list = convert_vowels_to_uppercase(input_list)
print(result_list)
