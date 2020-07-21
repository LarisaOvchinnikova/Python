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

word = "additional"
print(word.rindex("a")) # 8 (индекс первой буквы "a" в строке)
# print(word.rindex("b"))  # ValueError: substring not found

text = "My eyes are blue"
print(text.index("blue")) # 8 (индекс вхождения  строки "blue")

word = "My flowers are nice"
print(word.index("nice")) # 12 (индекс вхождения  строки "nice")

text = "Be loyal to the one who is loyal to you."
print(text.count("o"))

text = "To be or not to be"
print(text.count("be"))   # 2

a = 8
b =