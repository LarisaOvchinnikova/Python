from time import sleep

def fib(length = 10, n1 = 1, n2 = 1):
    result = []
    for i in range(length):
        result.append(n1)
        #sleep(0.5)
        n1, n2 = n2, n1 + n2
    return result

def fib_gen(length = 20, n1 = 1, n2 = 1):
    for i in range(length):
        #sleep(0.5)
        n1, n2 = n2, n1 + n2
    yield n1

# fib_seq = fib_gen()
# for i in fib_seq:
#     print(i)
# if 144 in fib_seq:
#     print("yes")


# arr = fib()
# print(arr[5])

# def my_gen():
#     for i in range(10):
#         sleep(0.5)
#         yield i # вернуть значение и не прекращать работу
#
# first = my_gen()
# print(next(first))  #0
# print(next(first))  #1
# print(next(first))  #2
# print(next(first))  #3

# for i in range(10):
#     print(next(first))

# i = iter(range(10))

# lst = [1,2,3,4,5]
# lst = iter(lst)
# print(next((lst)))
# print(next((lst)))

def infinite():
    i = 0
    while True:
        yield i
        i += 1


x = infinite()
print(next(x))
for i in range(100):
    print(next(x))