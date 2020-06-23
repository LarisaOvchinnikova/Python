# написать тест автоматически: ctrl + shift + T на имени функции
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def fibonacci(n):
    return n