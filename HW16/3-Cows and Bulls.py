from random import randint


secret_lst = []
while len(secret_lst) < 4:
    digit = randint(0, 9)
    if len(secret_lst) == 0 and digit == 0:
        continue
    if not str(digit) in secret_lst:
        secret_lst.append(str(digit))
#print(secret_lst)
secret = "".join(secret_lst)
#print(secret)
str = ""
number = input("Enter 4-digit number: ")
cows = 0
bulls = 0
while number != secret:
    number_lst = list(number)
    for i in range(4):
        if number_lst[i] == secret_lst[i]:
            str = str + number_lst[i]
            bulls += 1

        elif number_lst[i] in secret_lst:
            print(f"* digit {number_lst[i]} true, but on other position ")
            str = str + "_"
            cows += 1
        else:
            str = str + "_"
    print(str)
    print(f"{cows} cows, {bulls} bulls")
    cows = 0
    bulls = 0
    str = ""
    number = input("Enter 4-digit number: ")
print(f"You got it! It was {secret}")