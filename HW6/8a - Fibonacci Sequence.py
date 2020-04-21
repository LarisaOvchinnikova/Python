def fibonacci_sequence(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[-2] + fib[-1])
    strin = []
    for i in fib:
        strin.append(str(i))
    print(str)
    # return fib  # array of numbers
    return " ".join(strin)
print(fibonacci_sequence(10))