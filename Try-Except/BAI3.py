'''Write a program that takes a list of numbers and calculates the sum of their
squares. Handle the TypeError that can occur if a non-numeric value is
encountered. Use the finally clause to print the final sum'''
n  = int(input())
lst = []
for i in range(n):
    lst.append(input())
def sum_squares():
    sum = 0
    try:
        for k in lst:
            sum += int(k) ** 2
    except TypeError:
        print("The error is: TypeError")
    finally:
        print("Final sum: ", sum)
print(sum_squares())