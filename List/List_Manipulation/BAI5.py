n = int(input())
lst = [int(input()) for i in range(n)]
new_lst = []
def sum_other_elements():
    for x in lst:
        sum = 0
        c = lst.index(x)
        lst.remove(x)
        for k in lst:
            sum = sum + k
        lst.insert(c,x)
        new_lst.append(sum)   
    return new_lst
print(sum_other_elements())