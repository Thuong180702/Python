#Write a function that takes a list of strings as input and returns a new list containing the strings sorted by their lengths in descending order. If two strings have the same length, sort them lexicographically
n = int(input())
lst = []
a = []
def sapxep():
    for i in range(n):
        lst.append(input())
    for k in lst:
        lst.sort(key= lambda k: (len(k),k), reverse= True)
    return lst
print(sapxep())
