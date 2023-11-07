def sum_except_self(nums):
    total_sum = sum(nums)
    result = [total_sum - num for num in nums]
    return result


input_nums = [1, 2, 3, 4]
result_list = sum_except_self(input_nums)
print(result_list)
