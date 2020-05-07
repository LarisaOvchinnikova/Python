#from random import randint
import random
for i in range(10):
    x = random.randint(1,10)
    #x = randint(1,5)
    print(x)

fruits = ["banana", "orange", "lemon"]
print(fruits[random.randint(0, len(fruits)-1)])
print(random.choice(fruits))

print(random.random())  #float
x = random.random()
print(round(x,2))

x = random.uniform(1,100)  # float 1-100
print(round(x,2))
