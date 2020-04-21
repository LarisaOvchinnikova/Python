def isprime(num):
    if num == 1:
        return False
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    return True
print(isprime(7))
print(isprime(11))
print(isprime(6))
print(isprime(8))
print(isprime(2))
print(isprime(1))