def calculate_percentage(total, *values):
    total_sum = sum(values)

    list_percent = []

    for value in values:
        percent = (value / total_sum) * 100
        list_percent.append(percent)

    return list_percent

total_value = 1000
values = [250, 350, 400]
result = calculate_percentage(total_value, *values)
print(result)
