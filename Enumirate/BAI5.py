#Write a program that takes a list of strings and prints each string along with its index, skipping strings that start with a vowel
n = int(input())
lst = []
indices = []
new_strings = []
vowels = ['a', 'i', 'u', 'e', 'o', 'A', 'I', 'U', 'E', 'O']
for i in range(n):
    lst.append(input())
for k, string in enumerate(lst):
    if string[0] not in vowels:
        indices.append(k)
        new_strings.append(string)
print(list(zip(indices,new_strings)))