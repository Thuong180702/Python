#Write a program that takes a list of numbers and prints the indices of the numbers that are perfect squares
import math
import fractions
n = int(input())
lst = []
indices = []
new_lst = []
for i in range(n):
    lst.append(int(input()))
print(lst)
def is_perfect_square(num):
    if num >= 0:
        a = int(math.sqrt(num))
        return ((a*a) == num)
    return False
for k, num in enumerate(lst):
    if is_perfect_square(num):
        indices.append(k)
        new_lst.append(num)
print(list(zip(indices, new_lst)))