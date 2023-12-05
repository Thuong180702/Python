#Write a function that takes a list and returns a new list containing every second element in reverse order
'''n = int(input())
lst = []
a = []
def bai1():
    for i in range(n):
        lst.append(input())
    for k in lst:
        a.append(k[1])
    b = a[::-1]
    return b
print(bai1())'''

'''n = int(input())
lst = []
a = []
def bai1():
    for i in range(n):
        lst.append(input())
    a = lst[1][::-1]
    return a
print(bai1())
'''
n = int(input())
lst = []
a = []
def evenelement():
    for i in range(n):
        lst.append(int(input()))
    '''for k in range(len(lst)):
        if k % 2 != 0:
            a.append(lst[k])
    a.reverse()
    return a'''
    return lst[-2::-2]
print(evenelement())