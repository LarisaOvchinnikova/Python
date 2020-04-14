def add(a, b):
    return a + b

print(add(3,4))


def minimum(a,b):
    if a < b:
        return a
    else:
        return b

print(minimum (5, 1))

def sum(a, b, c):
    return a + b + c

print(sum(1,2,3))

def convert(f):
    c = (f - 32) * 5 / 9
    return round(c, 2)
print(f"today is {convert(100)} degrees")
# ----------------------------------
arr = [1, 2, 3]
def func():
    arr.append(4)            # change global array

func()
print(arr)                   # print [1, 2, 3, 4]
# ----------------------------------