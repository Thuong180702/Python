'''Write a program that attempts to open a file named "data.txt" and write some
content to it. Handle the PermissionError and print an appropriate error
message. Use the finally clause to close the file, even if an exception occurs'''
try:
    with open("C:/Users/This PC/OneDrive - The University of Technology/Documents/KÌ 1 NĂM 4/LẬP TRÌNH PYTHON/data.txt", "w") as file:
        file.write("Ton That\n")
        file.write("Tien")
        print("Da viet xong")

except PermissionError:
    print("Error: Failed to write to file. Please check the permissions.")

finally:
    file.close()
    print("Da dong file")