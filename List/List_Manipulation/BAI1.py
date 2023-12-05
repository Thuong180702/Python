n = int(input())
lst = []
def characters_vowel():
    for i in range(n):
        lst.append(input())
    for k in lst:
        if len(k) <= 5 or (k[0] != 'a' and k[0] != 'i' and k[0] != 'u' and k[0] != 'e' and k[0] != 'o'):
            lst.remove(k)
    return lst
print(characters_vowel())