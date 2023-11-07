def product_of_others(input_list):
    product_list = []
    total_product = 1

    for number in input_list:
        total_product *= number

    for number in input_list:
        product_list.append(total_product // number)

    return product_list


input_list = [2, 3, 4, 5]
result_list = product_of_others(input_list)
print(result_list)
