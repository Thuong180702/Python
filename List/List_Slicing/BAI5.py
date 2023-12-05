n = int(input())
lst = []
name = []
domain = []
for i in range(n):
    lst.append(input())
for k in lst:
    for j in range(len(k)):
        if k[j] == "@":
            name.append(k[0:j])
            domain.append(k[j+1:])
print("name =", name)
print("domain =", domain)