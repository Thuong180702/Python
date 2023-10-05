def calculate_median(*args):
    num_list = list(args)

    return sum(num_list)/len(num_list)

print(calculate_median(3, 1, 4, 1, 5, 9))