print("Nhap so: ", end="")
n = int(input())
l = []

for i in range(0,n):
    l.append(int(input()))
    
print(f"Max = {max(l)}")
