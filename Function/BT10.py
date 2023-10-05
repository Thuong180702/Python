def find_odd_numbers(*args):
    odd_numbers = []

    for num in args:
        if num % 2 != 0:
            odd_numbers.append(num)

    return odd_numbers

print(find_odd_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9))
