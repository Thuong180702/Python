n = int(input())
lst = [input() for i in range(n)]
new_lst = [x for x in lst if len(x) >= 3 and (x[0] == 'a' or x[0] == 'i' or x[0] == 'u' or x[0] == 'e' or x[0] == 'o')]
print(new_lst)