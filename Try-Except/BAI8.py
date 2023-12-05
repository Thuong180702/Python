'''Write a program that takes a list of strings and converts each string to uppercase.
Handle the AttributeError that can occur if a string does not have the upper()
method. Use the finally clause to print the final list of uppercase strings'''
n = int(input())
lst = []
new_lst = []
for i in range(n):
    lst.append(input())
try:
    for k in lst:
        a = k.upper()
        new_lst.append(a)
except:
    print("The error is:  a string does not have the upper() method")
finally:
    print(new_lst)