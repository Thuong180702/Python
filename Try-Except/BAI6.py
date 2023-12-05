'''Write a program that asks the user to enter a number and calculates its square
root. Handle the ValueError that can occur if the input is negative and print an
appropriate error message. Use the finally clause to print a message indicating the
end of the program'''
import math
n = float(input())
try:
    b = math.sqrt(n)
    print(b)
except ValueError:
    print("The error is: The input is negative")
finally:
    print("Program ended")