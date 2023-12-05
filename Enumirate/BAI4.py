#Write a program that takes a list of integers and prints the indices of the numbers that are divisible by 3
n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))
indices = []
number = []
for k, num in enumerate(lst):
    if num % 3 == 0:
        indices.append(k)
        number.append(num)
print(list(zip(indices,number)))