import string
from random import randint, choice

# print(string.digits)      # 0123456789
# print(string.punctuation) # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
# print(string.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)
#print(choice(string.punctuation))
level = int(input("Enter level of difficulty of password: 1 - easy, 2 - medium, 3 - strong: "))
if level == 1:
    s = string.digits + string.ascii_lowercase
    length = randint(5, 7)
elif level == 2:
    s = string.digits + string.ascii_letters
    length = randint(7, 9)
else:
    s = string.digits + string.ascii_letters + string.punctuation
    length = randint(10, 15)

password = "".join([choice(s) for i in range(length)])
print(f"Your password is: {password}")