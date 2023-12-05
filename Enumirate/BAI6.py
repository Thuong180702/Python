#Write a program that takes a list of numbers and prints the indices of the numbers that are greater than the average of the list
n = int(input())
lst = []
indices = []
new_lst = []
sum = 0
average = 0
for i in range(n):
    lst.append(int(input()))
for i in lst:
    sum += i
average = sum/len(lst)
print(average)
for k, num in enumerate(lst):
    if num > average:
        indices.append(k)
        new_lst.append(num)
print(list(zip(indices, new_lst)))