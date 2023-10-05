n = 0
while n<=0:
    print("Nhap so: ", end="")
    n = int(input())
Gt = 1
for i in range(1,n+1):
    Gt *= i 

print(f"{n}! = {Gt}")