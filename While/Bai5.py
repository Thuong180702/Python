l = []
while True:
    print("Nhap so: ", end="")
    i = int(input())
    if i == -1:
        break
    l.append(i)
    print(f"TB ={sum(l)/len(l)}")