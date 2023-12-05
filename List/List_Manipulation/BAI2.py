n = int(input())
lst = []
a = []
b = []
def rearranges():
    for i in range(n):
        lst.append(int(input()))
    for k in lst:
        if k % 2 == 0:
            a.append(k)
        if k % 2 != 0:
            b.append(k)
    a.extend(b)
    return a
print(rearranges())