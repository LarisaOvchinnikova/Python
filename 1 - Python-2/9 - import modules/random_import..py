import random
#import antigravity

from random import randint, choice

# print(random.randint(10))  # сл.число от 0-9
# a = random.randint(1, 10)
a = randint(1, 10)
x = [1,2,3,4,5]
print(choice(x))
if a in x:
    print('yes')
else:
    print('no')