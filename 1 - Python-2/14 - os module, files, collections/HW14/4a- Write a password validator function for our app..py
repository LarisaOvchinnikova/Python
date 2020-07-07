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


    vals = {
        'You need at least one uppercase letter': count_upper >= 1,
        'You need at least two lowercase letters': count_lower >= 2,
        'You need at least one digit': count_digit >= 1,
        'Length must be between 6 and 12 characters': 6 <= len(password) <= 12
    }
    output = ""
    for msg, condition in vals.items():
        if not condition:
            output += f"{msg}.\n"

    # if not output:
    #     return True
    # else:
    #     return output

    return True if not output else output

print(password_validator("Alic11"))
print(password_validator("laRisa171"))