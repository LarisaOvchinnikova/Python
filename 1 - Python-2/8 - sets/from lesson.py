# вложенные массивы
shop = [("Pizza", 9.99, 2), ("Sushi", 19.99, 3), ("Ice cream", 5.99, 1)]
print(shop[1])     # ('Sushi', 19.99, 3)
print(shop[1][0])  # 'Sushi'

for item in shop:
    print(item)
# ('pizza', 9.99, 2)
# ('sushi', 19.99, 3)
# ('Ice cream', 5.99, 1)
print(len(shop)) # 3

for item in shop:
    print(item[0])
# Pizza
# Sushi
# Ice cream

for item in shop:
    print(item)
    for elem in item:
        print(elem)

# ('Pizza', 9.99, 2)
# Pizza
# 9.99
# 2
# ('Sushi', 19.99, 3)
# Sushi
# 19.99
# 3
# ('Ice cream', 5.99, 1)
# Ice cream
# 5.99
# 1
# Задача. Найти количество гласных и согласных в каждм слове массива:
text = ["Hello", "banana", "Pizza", "apple"]
for word in text:
    vowels = 0
    consonants = 0
    for char in word:
        if char.lower() in "aeuio":
            vowels += 1
        else:
            consonants += 1
    print(f"The word is {word}: \nVowels = {vowels} and consonants = {consonants}")

# функция print
text = ["Hello", "banana", "Pizza", "apple"]
for word in text:
    for char in word:
        print(char)
    print()

print("Hi")
print("World") # печатает каждое слово с новой строки по дефолту
print("Hi\nWorld") # то же самое

print ("Hi", "Hey") # разделяет автоматом пробелом
print ("Hey", end = '*')
print ("world")  # Hey*world


text = ["Hello", "banana", "Pizza", "apple"]
for word in text:
    for char in word:
        print(char, end =" ")  # печатает не в столбик а в строку через пробел
    print()

table = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"],
]
print(table)  # [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]

table[0][2] = "X"
print(table) # [['-', '-', 'X'], ['-', '-', '-'], ['-', '-', '-']]

