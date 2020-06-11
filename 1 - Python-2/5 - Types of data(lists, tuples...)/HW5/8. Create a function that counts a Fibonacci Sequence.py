def fibonacci(n):
    if n == 0:
        return []
    elif n == 1:
        return [0]
    fib = [0, 1]
    for  i in range(2, n):
        fib.append(fib[i-2] + fib[i-1])
    return fib


print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(10))