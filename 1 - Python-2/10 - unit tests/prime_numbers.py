def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % 2 == 0:
            return False
    return True