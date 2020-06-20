import string
from random import choice

print(string.digits)      # 0123456789
print(string.punctuation) # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
print(string.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(choice(string.punctuation))
s = string.digits + string.punctuation + string.ascii_letters
password = "".join([choice(s) for i in range(10)])
print(password)