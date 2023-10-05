input_string = input("Nhập chuổi: ")

prefix = input("Prefix: ")

if input_string.endswith(prefix):
    print(f"Đúng")
else:
    print(f"Sai")