n = int(input("Nhập số: "))
l = [i for i in range(2,n)]
a=0
print(list(map(lambda i: all(n%i!=0) ,l)))

