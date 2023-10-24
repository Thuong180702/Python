num = 1

while num <= 9:
    print(f"Bảng cửu chương của {num}:")
    i = 1
    while i <= 10:
        result = num * i
        print(f"{num} x {i} = {result}")
        i += 1
    print()
    num += 1
