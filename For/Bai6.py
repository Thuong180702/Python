print("Nhap so: ", end="")
n = int(input())
s = 0

for i in range(0,n+1,2):
    print(i)
    s = s+i

print(f"sum = {s}")