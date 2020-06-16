def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    return True


print(is_prime(1))
print(is_prime(2))
print(is_prime(-1))
print(is_prime(11))
print(is_prime(7))
print(is_prime(20))