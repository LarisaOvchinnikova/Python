myvar1 = True
myvar2 = False
myvar = 4 == 3
print(myvar)
fruit = "banana"
print("a" in fruit)   # True
print("u" in fruit)   # False

vowels = "aeuio"
print("b" in vowels)
fruit = "banana"
print("a" in fruit)   # True
print("u" in fruit)   # False

vowels = "aeuio"
print("b" in vowels)

if "a" in vowels:
    print("a is vowel!")

print(bool(0))
print(bool(''))
print(bool([]))
print(bool(None))
print(bool({}))

num = 0
if num:
    print("number is True")
else:
    print("number is False")

st = ""
if st:
    print("string is not empty")
else:
    print("string is empty")

a = int(input("Enter a: "))
b = int(input("Enter b: "))
if b > 0:
    linear = f"{a} x + {b}"
else:
    linear = f"{a} x - {-b}"
print(linear)    