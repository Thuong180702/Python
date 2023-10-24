def generate_subsets(input_set, max_length):
    def backtrack(start, current_subset):
        if len(current_subset) <= max_length:
            all_subsets.add(frozenset(current_subset))
        if len(current_subset) == max_length:
            return
        for element in input_set:
            if element not in current_subset:
                current_subset.add(element)
                backtrack(element, current_subset)
                current_subset.remove(element)

    all_subsets = set()
    backtrack(None, set())
    return all_subsets

input_set = {1, 2, 3}
max_length = 2
result = generate_subsets(input_set, max_length)
print(result)
