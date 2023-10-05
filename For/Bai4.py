print("Nhap so tuoi :")
tuoi = int(input())
print("Nhap gioi tinh(nam/nu) :")
sex = input()

if sex == "nam":
    print("Du dk") if tuoi >= 65 else print("K du dk")
else:
    print("Du dk") if tuoi >= 60 else print("K du dk")