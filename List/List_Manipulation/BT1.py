def filter_strings(strings):
    vowels = ["a", "e", "i", "o", "u"]
    filtered_strings = [s for s in strings if len(s) > 5 and s[0].lower() in vowels]
    return filtered_strings


input_strings = ["apple", "banana", "cherry", "orange", "grape", "elephant", "kiwi"]
filtered_list = filter_strings(input_strings)
print(filtered_list)
