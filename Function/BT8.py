def calculate_product(*args):
    product = 1

    for num in args:
        product *= num

    return product

print(calculate_product(3,5,3.5))