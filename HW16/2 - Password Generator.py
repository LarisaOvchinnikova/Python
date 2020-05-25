import string
import random
#Воспользуйтесь модулем string чтобы получить разные символы для пароля
s_p = string.punctuation
s_l = string.ascii_letters
s_d = string.digits
easy_str = list(s_l)
med_str = list(s_d + s_l)
strong_str = list(s_d + s_l + s_p)
level = input("Enter level of difficulty for password: 1 - easy, 2 - medium, 3 - strong: ")
if level == "1":
    length = 5
    password = "".join([random.choice(easy_str) for i in range(length)])

elif level == "2":
    length = 7
    password = "".join([random.choice(med_str) for i in range(length)])
else:
    length = 12
    password = "".join([random.choice(strong_str) for i in range(length)])
print(password)

