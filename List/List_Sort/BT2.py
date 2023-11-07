def sort_dictionaries_by_age_descending(dict_list):
    return sorted(dict_list, key=lambda x: x["age"], reverse=True)


data = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35},
    {"name": "David", "age": 28},
]

sorted_data = sort_dictionaries_by_age_descending(data)
print(sorted_data)
