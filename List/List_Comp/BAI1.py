n = int(input())
lst = [int(input()) for i in range(n)]
new_lst = list(map(lambda x: x*2 if x % 3 == 0 else x, lst))
print(new_lst)