n = int(input())
lst = []
a = []
def numbercharacters():
    for i in range(n):
        lst.append((input()))
    for k in lst:
        lst.sort(key = lambda k: len(k))
    return lst
print(numbercharacters())
