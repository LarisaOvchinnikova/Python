def password_validator(password):
    res = 0
    count1 = 0
    count2 = 0
    count3 = 0
    for letter in password:
        if letter.islower():
            count1 += 1
        if letter.isdigit():
            count2 += 1
        if letter.isupper():
            count3 += 1
    if count1 >= 2:
        res += 1
    if count2 >= 1:
        res += 1
    if count3 >= 1:
        res += 1
    return 6 <= len(password) <= 12 and res == 3

print(password_validator("Alice1%&&&"))