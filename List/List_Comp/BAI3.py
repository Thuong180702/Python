n = int(input())
lst = [input() for i in range(n)]
new_lst = [x[::-1] for x in lst]
print(new_lst)