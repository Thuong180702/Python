def reverse_middle_three(input_list):
    if len(input_list) < 3:
        return input_list

    middle_start = (len(input_list) - 3) // 2
    middle_end = middle_start + 3

    result_list = (
        input_list[:middle_start]
        + input_list[middle_start:middle_end][::-1]
        + input_list[middle_end:]
    )
    return result_list


input_list = [1, 2, 3, 4, 5, 6, 7]
result_list = reverse_middle_three(input_list)
print(result_list)
