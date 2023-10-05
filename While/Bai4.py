while True:
    print("Nhap so: ", end="")
    Num = int(input())
    Nt = 0
    for i in range(1, Num+1):
        if Num % i == 0:
            Nt += 1
    if Nt ==2 or Num <=3:
        print("SNT")
    else:
        print("KPSNT")