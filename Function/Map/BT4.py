n = int(input("Nhập số: "))
l = [i for i in range(2, n)]
a = 0
List_nt =list(map(lambda i:1 if n % i != 0 else 0, l))

if 0 in List_nt:
    print("Kphai")
else:
    print("Phai")