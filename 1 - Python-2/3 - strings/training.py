# word = "summer"
# print("*" * 8)
# print("*summer*")
# print("*" * 8)
# name = "John"
# print("Hello boss") if name == "Bill" else print("Hello guest")
#
# print("a" in "apple")
# word = "accessories"
# i = word.find("a")
# print(i)
# print(word.find("s"))
# print(word.find("b"))
# print(word.find("s", 6)) # 10
# print(word.find("s", 6, 9)) # -1

# word = "september"
# print(word.rfind("a"))
# word = "september"
# print(word.index("e")) # 1 (индекс первой буквы "e" в строке)
# print(word.index("a")) # ValueError: substring not found

# word = "additional"
# print(word.rindex("a")) # 8 (индекс первой буквы "a" в строке)
# # print(word.rindex("b"))  # ValueError: substring not found
#
# text = "My eyes are blue"
# print(text.index("blue")) # 8 (индекс вхождения  строки "blue")
#
# word = "My flowers are nice"
# print(word.index("nice")) # 12 (индекс вхождения  строки "nice")
#
# text = "Be loyal to the one who is loyal to you."
# print(text.count("o"))
#
# text = "To be or not to be"
# print(text.count("be"))   # 2
#
# a = int(input("Enter the 1st number: "))
# b = int(input("Enter the 2nd number: "))
# c = int(input("Enter the 3rd number: "))
# print(f"Minimum is {min(a, b, c)}")
# print(f"Maximum is {max(a, b, c)}")
#
# word = "center"
# print(word.center(20))
#
# word = input("Enter word: ")
# width = int(input("Enter width of the box"))
# if width < len(word):
#     print("ERROR")
# else:
#     print("*" * width)
#     print("*"  + word.center(width-2) + "*")
#     print("*" * width)
#
# print("      Ava")
# print("Charlotte")
# print("    Smith")
# print("my flowers are beautiful".capitalize())
# print("my flowers are beautiful".title())
# print("CODEWars".lower())
# print("aBcDe".swapcase()) # AbCdE
#
# num = "12"
# num = num.zfill(4)
# print(num)
#
# print("Hello world".startswith("H")) # True
# print("Hello world".startswith("h")) # False
# print("Hello world".endswith("rld")) # True
# print("Hello world".endswith("!")) # False

# vowels = "aeuio"
# letter = input("Enter letter: ")
# print(not letter.lower() in vowels)
#
# s = "sky!"
# print(s.isalpha())
# year = "2020"
# print(year.isdigit())
# print("23,5".isdigit())
# s = "May9"
# print(s.isalnum())
# print(" ".join(["a", "b", "c"]))
#
# name = "**Alice"
# print(name.lstrip("*"))
# print("     Hello world!  ". lstrip())
# password = "qwerty!!!"
# print(password.rstrip("!"))
# print("A like Python!    ". rstrip())
# s = "Sky is blue and the weather is beautiful"
# new_s = s.replace("is", "was")
# print(new_s)
# s = "Apples. bananas. limes. peaches. plums. Buy now. Low prices."
# new_s = s.replace(".", ",", 4)
# print(new_s)
#
# print(range(10))
#
# def say_hello():
#     print("Hello!")
#
# print(say_hello())
#
# x = 12
# print(type(x) == int)
# l= 0

# s = 'hfhghghfhfhhf'
# for letter in s:
#     if letter.isdigit():
#         print("yes")
#         break
# else:
#     print ('no')

# arr = [5, 2, 1, 4, 5, 2, 3, 4, 2, 0]
# print(arr.index(1))  # 2
#
# words = ["apple", "kiwi", "banana", "peach"]
# print("apple" in words) # True
# print("apples" in words) # False


# Перевод в двоичную систему 1 case
s = 5
# print(bin(s))
# print(type(bin(s))) # str
p = (bin(s))[2:]
print(p)
# Перевод в двоичную систему 2 case
n = 5
b = ''
while n > 0:
    b = str(n % 2) + b
    n = n // 2
print(b)