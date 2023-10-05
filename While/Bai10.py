print("Nhap so: ", end="")
n = int(input())
S = 0
while n>0:
    if n % 2 ==0:
        S += n
    n -= 1
print(f"Tổng các số chẵn: {S}")