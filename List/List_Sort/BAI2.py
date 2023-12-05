lst = [
    {'name': 'Tien', 'age': 35},
    {'name': 'Hoang', 'age': 30},
    {'name': 'Long', 'age': 29}
]
a = []
def sortage():
    lst.sort(key = lambda x:  x.get('age'), reverse = True)
    for x in lst:
        a.append(x)
    return a
print(sortage())