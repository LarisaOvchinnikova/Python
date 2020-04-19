def isprime(num):
    countOfDividers = 0
    for i in range(1, num + 1):
        if num % i == 0:
            countOfDividers += 1
    return countOfDividers == 2
print(isprime(7))
print(isprime(11))
print(isprime(6))
print(isprime(8))
print(isprime(2))