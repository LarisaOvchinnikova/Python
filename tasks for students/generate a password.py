import random
strLower = "qwertyuiopasdfghjklzxcvbnm"
strUpper = strLower.upper()
strDigits = '1234567890'
strTotal = strLower+strUpper+strDigits;
# create password from 12 chars
password = ''
for i in range(12):
    c = random.choice(strTotal)
    password = password + c
print(password)

password1 = "".join([random.choice(strTotal) for i in range(12)])
print(password1)