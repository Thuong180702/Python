n = int(input())
lst = []
def second_character():
    for i in range(n):
        lst.append(input())
    for k in lst:
        lst.sort(key= lambda k: k[1])
    return lst
print(second_character())