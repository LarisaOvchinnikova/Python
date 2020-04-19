def fibonacci_sequence(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-2] + fib[i-1])
    return fib
print(fibonacci_sequence(10))