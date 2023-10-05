dic = {"toan":8,"ly":10,"hoa":7}
dic = dict(sorted(dic.items(), key= lambda x: x[1]))
print(dic)