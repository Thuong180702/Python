#Write a program that takes a list of numbers and returns a new list containing only the prime numbers along with their indices
n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))
def prime(num):
    count = 0
    if num <= 1:
        return False
    else:
        for i in range(1, num + 1):
            if num % i == 0:
                count += 1
        if count <= 2:
            return True
        else:
            return False
def prime_indices(lst):
    indices = []
    new_lst = []
    for k, num in enumerate(lst):
        if prime(num):
            new_lst.append(num) 
            indices.append(k)
    return zip(indices, new_lst)
print(list(prime_indices(lst)))


'''def is_prime(num):
    if num <= 1:
        return False
    for I in range(2, int(num**0.5) + 1):
        if num % I == 0:
            return False
    return True
def get_prime_indices(numbers):
    primes = []
    indices = []
    for i, num in enumerate(numbers):
        if is_prime(num):
            primes.append(num)
            indices.append(i)
    return zip(indices, primes)
numbers = [17, 23, 12, 31]
primes_indices = get_prime_indices(numbers)
print(list(primes_indices))'''