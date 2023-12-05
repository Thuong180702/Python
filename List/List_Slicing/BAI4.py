n = int(input())
lst = []
def vowel_uppercase():
    for i in range(n):
        lst.append(input())
    for k in range(len(lst)):
        for j in lst[k]:
            if j == 'a' or j == 'i' or j == 'e' or j == 'o' or j == 'u':
                a = j.upper()
                b = lst[k].replace(j, a)
                lst[k] = b
    return lst
print(vowel_uppercase())