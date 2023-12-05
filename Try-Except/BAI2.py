'''Write a program that reads a file named "data.txt" and prints its contents.
Handle the FileNotFoundError and print an appropriate error message. Use
the finally clause to close the file, even if an exception occurs'''
try:
    with open("C:/Users/This PC/OneDrive - The University of Technology/Documents/KÌ 1 NĂM 4/LẬP TRÌNH PYTHON/data.txt", "r") as file:
        contents = file.read()
        print(contents)
except FileNotFoundError:
    print("The error is: FileNotFoundError")
finally:
    file.close()