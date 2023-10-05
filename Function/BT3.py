def TB(l):
    return sum(l)/len(l)
a = int(input("Chiều dài chuổi: "))
l = []
print("Nhập chuổi")
for i in range(a):
    l.append(int(input()))
print(f"Trung bình cộng là {TB(l)}")