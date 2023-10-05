dict1 ={"toan":8,"ly":10,"hoa":7}
dict2 ={"toan":8,"van":10,"hoa":7}

keys = []
for key in dict1:
    if key in dict2:
        keys.append(key)
print(keys)