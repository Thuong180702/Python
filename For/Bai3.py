print("Nhap so nam: ")
nam = int(input())

if nam % 4 == 0 and nam % 100 !=0 and nam % 400 !=0 or nam % 400 == 0:
    print("Nam nhuan")
else:
    print("Nam k nhuan")