def TB(l):
    for i in range(len(l)):
        l[i] = l[i] - 2*l[i]
    return l
a = int(input("Chiều dài chuổi: "))
l = []
print("Nhập chuổi")
for i in range(a):
    l.append(int(input()))
print(f"Chuỗi nguyên âm là {TB(l)}")