#Write a program that takes a string and prints all the vowels along with their indices
string = input()
indices = []
vowels = []
for k, character in enumerate(string):
    if character == 'a' or character == 'i' or character == 'u' or character == 'e' or character == 'o':
        indices.append(k)
        vowels.append(character)
print(list(zip(indices, vowels)))