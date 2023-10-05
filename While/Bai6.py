l = []
while True:
    print("Nhap so: ", end="")
    n = int(input())
    if n == 0:
        break
    print("Nhap chuoi so: ", end="")
    for i in range(0,n):
        l.append(int(input()))
    print(f"Max ={max(l)}")