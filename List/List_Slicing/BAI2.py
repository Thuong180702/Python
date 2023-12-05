#Write a function that takes a list and returns a new list with the middle three elements of the original list reversed
'''n = int(input())
lst = []
a = []
def reverse_middle_three_elements():
    for i in range(n):
        lst.append(input())
    mid = len(lst) // 2
    a.append(lst[mid+1])
    a.append(lst[mid])
    a.append(lst[mid-1])
    lst[mid-1:mid+2] = a
    return lst
print(reverse_middle_three_elements())
'''

n = int(input())
lst = []
a = []
def reverse_middle_three_elements():
    for i in range(n):
        lst.append(input())
    mid = len(lst) // 2
    return lst[:mid-1] + lst[mid+1:mid-2:-1] + lst[mid+2:]
print(reverse_middle_three_elements())