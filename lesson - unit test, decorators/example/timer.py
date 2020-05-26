import time

def timer(func, x, y):
    start = time.time()
    result = func(x, y)

    end = time.time() - start
    print("Time elapsed ", round(end, 3))
    return result

def add(x,y = 10):
    time.sleep(0.5)
    return x + y
def sub(x,y):
    time.sleep(0.5)
    return x - y
def mul(x,y):
    time.sleep(0.5)
    return x * y

print("add(1,2) --> ", timer(add, 1, 2))
print("sub(1,2) --> ", timer(sub, 1, 2))
print("mul(1,2) --> ", timer(mul, 1, 2))