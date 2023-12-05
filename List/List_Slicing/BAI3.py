n = int(input())
lst = []
a = []
def removefirstandlast():
    for i in range(n):
        lst.append(input())
    for k in lst:
        a.append(k[1:len(k)-1])
    return a
print(removefirstandlast())
