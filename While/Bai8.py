l = []
while True:
    print("Nhap so: ", end="")
    n = int(input())
    if n == 0:
        break
    print("Nhap chuoi so: ", end="")
    for i in range(0,n):
        l.append(int(input()))
    total = 0
    for i in l:
        if i %3 == 0:
            total += i
    print(f"Tổng các số chia hết cho 3 là: {total}")