print("Nhap so: ", end="")
n = int(input())
s3 =  sum(i for i in range(0,n+1,3))
s5 =  sum(i for i in range(0,n+1,5))

print(f"Tong so chia het cho 3 = {s3}")
print(f"Tong so chia het cho 5 = {s5}")