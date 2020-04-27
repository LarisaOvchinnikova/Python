y = list(range(1,11))
print(y)
x = [1,2,3,10,5,4,7,6,8]
print(x)
# найти какого элемента из y не хватает в х
setY = set(y)
setX = set(x)
print(setY - setX)  # --> 9

users1 = ["user1", "user 4", "user67"]
users2 = ["user1", "user67", "user56", "user11111"]
print(set(users1) - set(users2))
print(set(users1) & set(users2))  #те, кто есть в двух сетах


x = "masha"
name1 = set(x)
y = "misha"
name2 = set(y)
print("1 - ", name1)
print("2 - ", name2)
print(name1 & name2)
print(name1 - name2)
print(name2 - name1)

word1 = set("quit")
word2 = set("qiut")
print(word1 == word2)

#iteration

for i in word1:
    print(i)

# for i in range(len(word1))   -----> ERROR
    print(i)

#set comprehension
word = set("larisa")
print({letter.upper() for letter in word })
#dict comprehension
word = "LARISA"
x = {letter: word.count(letter) for i, letter in enumerate(word)}
print(x)

x = {}  # - это словарь
x = set() # - это пустой set

print(x)
x.add(2)
x.add(5)
#print(x)
x.update("a", "b", "c")
x.update("5")
print(x)