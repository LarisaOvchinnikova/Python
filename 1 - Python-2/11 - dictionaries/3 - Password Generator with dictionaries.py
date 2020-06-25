from string import digits, ascii_letters, punctuation
from random import choice


def gen_password(level):
    choose = {
        "easy": digits,
        "medium": digits + ascii_letters,
        "strong": digits + ascii_letters + punctuation
    }
    # s = ""
    # for i in range(10):
    #     s += choice(choose[level])

    return "".join([choice(choose[level]) for i in range(10)])


level = input("Enter level of difficulty of password: easy, medium, strong: ")
print(f"Your password is: {gen_password(level)}")
