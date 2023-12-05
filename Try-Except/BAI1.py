'''Write a program that takes two numbers as input and calculates the division
of the first number by the second number. Handle the ZeroDivisionError and
print an appropriate error message. Use the finally clause to print a message
indicating the end of the program'''
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
try:
    result = a/b
    print("Result is: ", result)
except ZeroDivisionError:
    #raise ZeroDivisionError("Division by zero is not allowed")
    print("The error is: Division by zero is not allowed")
finally:
    print("Program Ended")