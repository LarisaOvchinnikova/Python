def password_validator(password):
    res = 0
    s_res = ''
    count_lower = 0
    count_digit = 0
    count_upper = 0
    for letter in password:
        if letter.islower():
            count_lower += 1
        if letter.isdigit():
            count_digit += 1
        if letter.isupper():
            count_upper += 1
    if count_lower >= 2:
        res += 1
    else:
        s_res = "You need at least 2 lowercase letters\n "
    if count_digit >= 1:
        res += 1
    if count_upper >= 1:
        res += 1
    return 6 <= len(password) <= 12 and res == 3

print(password_validator("Alice1%&&&"))