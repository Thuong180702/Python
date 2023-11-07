def sort_strings_by_unique_characters(input_list):
    def unique_chars_count(s):
        return len(set(s))

    return sorted(input_list, key=unique_chars_count)


input_list = ["apple", "banana", "cherry", "date", "fig"]
sorted_list = sort_strings_by_unique_characters(input_list)
print(sorted_list)
