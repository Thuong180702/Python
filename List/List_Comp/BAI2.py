#Write a list comprehension that takes a list of strings and returns a new list containing the lengths of each string in uppercase
n = int(input())
lst = [input() for i in range(n)]
new_lst = [str(len(x)).upper() for x in lst]
print(new_lst)