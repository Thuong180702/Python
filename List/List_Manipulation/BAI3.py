n = int(input())
new_lst = []
lst = [int(input()) for i in range(n)]
def other_elements():
    for x in lst:
        mul = 1
        c = lst.index(x)
        lst.remove(x)
        for k in lst:
            mul = mul * k
        lst.insert(c,x)
        new_lst.append(mul)   
    return new_lst
print(other_elements())