def rearrange_even_odd(numbers):
    even_index = 0
    for odd_index in range(len(numbers)):
        if numbers[odd_index] % 2 == 0:
            numbers[even_index], numbers[odd_index] = (
                numbers[odd_index],
                numbers[even_index],
            )
            even_index += 1

    return numbers


input_numbers = [1, 2, 3, 4, 5, 6, 7, 8]
rearranged_list = rearrange_even_odd(input_numbers)
print(rearranged_list)
