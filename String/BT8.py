string = input("Họ và tên: ")
list_string = string.split()
for i in range(len(list_string)):
    list_string[i] = list_string[i].capitalize()
print(" ".join(list_string))