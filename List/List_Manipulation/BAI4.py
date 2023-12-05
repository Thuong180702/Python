n = int(input("Nhap so phan tu cua mang 1: "))
m = int(input("Nhap so phan tu cua mang 2: "))
lst1 = []
lst2 = []
lst = []
def commonelements():
    print("Nhap cac phan tu cua mang 1: ")
    for i in range(n):
        lst1.append(int(input()))
    print("Nhap cac phan tu cua mang 2: ")
    for k in range(m):
        lst2.append(int(input()))
    for u in lst1:
        if u in lst2:
            if u not in lst:
                lst.append(u)
    return lst
print(commonelements())
        