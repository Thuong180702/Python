#Implement a function that takes a list of integers and returns a new list where each element is the product of all the other elements in the original list
'''n = int(input())
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
print(other_elements())'''

'''n = int(input())
lst = [int(input()) for i in range(n)]
def product_of_others(lst):
    prod = 1
    for i in lst:
        prod *= i
    return [prod // i for i in lst]
print(product_of_others(lst))'''

n = int(input())
mul = 1
new_lst = []
lst = [int(input()) for i in range(n)]
def other_elements():
    for x in lst:
        mul = 1
        for k in lst:
            if k != x:
                mul = mul * k
        new_lst.append(mul)
    return new_lst
print(other_elements())