print("Nhap so: ", end="")
Num = int(input())
Nt = 0
for i in range(1, Num+1):
    if Num % i == 0:
        Nt += 1
if Nt == 2:
    if Num < 10:
        print("Phai")
    else:
        Num1 = str(Num)[::-1]
        if Num == int(Num1):
            print("Phai")
        else:
            print("k phai")
else:
    print("K phai so ng to")
