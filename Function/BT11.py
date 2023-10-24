def calculate_percentage(*args):
    total_sum = sum(values)

    list_percent = []

    for value in values:
        percent = (value / total_sum) * 100
        list_percent.append(percent)

    return list_percent

values = [250, 350, 400]
result = calculate_percentage(*values)
print(result)
