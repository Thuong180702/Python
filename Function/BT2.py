def area(a):
    return "chẵn" if a%2==0 else "lẽ"
a = int(input("Nhập số: "))
print(f"Là số {area(a)}")