n = int(input())
lst = []
def evennumber():
    for i in range(n):
        lst.append(int(input()))
    for k in lst:
        if k % 2 != 0:
            lst.remove(k)
    lst.sort(reverse=True)
    return lst
print(evennumber())