'''Write a program that takes a string as input and converts it to an integer.
Handle the ValueError that can occur if the input is not a valid integer. Use the
finally clause to print a message indicating the end of the program'''
string = input()
try:
    a = int(string)
    print(a)
except ValueError:
    print("The error is: ValueError")
finally:
    print("Program ended")
    