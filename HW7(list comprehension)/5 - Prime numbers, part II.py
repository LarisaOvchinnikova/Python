# Prime numbers, part II
# Create a function that return list of n prime numbers

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True
def prime_list(n):
    lst = []
    i = 2
    while (len(lst) < n):
        if isPrime(i):
            lst.append(i)
        i += 1
    return lst
print(prime_list(10))