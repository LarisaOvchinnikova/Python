arr1 = [ 1,2,3,4,5]
arr2 = [1,2,3]
for i in range(len(arr2)):
    print(arr1[i], arr2[i])


for x,y in zip(arr1, arr2):
    print(x, y)
print('----------================')
a=[1,2,3]
b =["a",'b','c']
z = []
for x,y in zip(a,b):
    z.append(x,y)
print(z)
print("===================")
for pair in zip(arr1, arr2):
    print(pair)

s1 = "abcde"
arr = [1,2,3,4,5]
for pair in zip(s1, arr):
    print(pair)

ar1 = [1, 2, 3, 4]
ar2 = "abc"
ar3 = ("x", "y", "z")
for pair in zip(ar1, ar2, ar3):
    print(pair)

print(list(enumerate("hello"))) # [(0, 'h'), (1, 'e'), (2, 'l'), (3, 'l'), (4, 'o')]
print(list(zip(ar1, ar2, ar3))) # [(1, 'a', 'x'), (2, 'b', 'y'), (3, 'c', 'z')]

x = dict([("a", 1), ("b", 2), ("c", 3)])
print(x) # {'a': 1, 'b': 2, 'c': 3}

a1 = ("z", "x", "y")
a2 = [1, 2, 3]
dct = dict(zip(a1, a2))
print(dct) # {'z': 1, 'x': 2, 'y': 3}

s = "hello"
length = len(s)
for pair in zip(range(length), s):
    print(pair)

# ===============================================
person = ("Jack", "123-23-34")
print(f"The person is {person[0]} with phone number {person[1]}")


class Person:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

p1 = Person("Jack", "123-23-34")
print(p1.name)

#============================
from collections import namedtuple

Person = namedtuple("Person", ["name", "phone_number"])
user1 = Person(name="Jack", phone_number="123-333-44")
print(user1) # Person(name='Jack', phone_number='123-333-44')
print(type(user1)) # <class '__main__.Person'>
print(isinstance(user1, tuple)) # True
print(user1.phone_number)
print(f"The person is {user1.name} with phone number {user1.phone_number}")

print(user1[0]) # Jack
print(user1[1]) # 123-333-44
print(len(user1)) # 2

Person = namedtuple("Person", ["name", "phone_number", "age"])
user1 = Person(name="Jack", phone_number="123-333-44", age=37)
print(user1.age)
test_user = Person("Alice", "212-111-11", 20)

user1 = Person(test_user[0], test_user[1], test_user[2])
print(user1)

# =============================
arr = [1, 2, 3, 4, 5]
print(1, 2, 3, 4, 5)

def add(x, y):
    return  x + y


def func(*iterable):
    print(iterable) #
    print(iterable[:4])


func(1,2,3,4,5)  # (1, 2, 3, 4, 5)  (1, 2, 3, 4)
# ------------------------------
def func(*iterable):
    return sum(iterable)


print(func(1,2,3,4,5)) # 15
#--------------------------------
def func(x, y, *iterable):
    return sum(iterable)


print(func(1,2,3,4,5)) # 12
# =================================
print(1,2,3,4,5, end=";") #keyword argument # 1 2 3 4 5;

def func(x, y, *iterable,**kwargs):
    print(x,y)
    print(iterable)
    print(kwargs)

print("-------------")
func(10,20, 30, 40, my_args="hello", text="bla-bla")

print(*[1,2,3,4]) # 1 2 3 4 (типа спред-оператор - превращает массив в набор элементов


# ----------
test_dct = {"name": "Bob",
             "phone_number": "12345",
             "age": 23}

user2 = Person(name="Jack", phone_number="123-333-44", age=37)
print(user2)
user3 = Person(**test_dct) # распакованный словарь
print(user3)

print(f"The person is {user1.name} with phone number {user1.phone_number}. He is {user1.age} years old")

# ===========
from collections import Counter
c = Counter()
c["a"] = 10
print(c["a"])  # 10
del c["a"]
print(c)
print(isinstance(c, dict))