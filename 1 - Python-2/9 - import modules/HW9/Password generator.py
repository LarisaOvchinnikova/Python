# https://www.codewars.com/kata/58ade2233c9736b01d0000b3

# You need to write a password generator that meets the following criteria:
#
# 6 - 20 characters long
# contains at least one lowercase letter
# contains at least one uppercase letter
# contains at least one number
# contains only alphanumeric characters (no special characters)
# Return the random password as a string.
#
# Note: "randomness" is checked by counting the characters used in the generated passwords - all characters should have less than 50% occurance.
# Based on extensive tests, the normal rate is around 35%.

import string
from random import randint, choice
def password_gen():
    s1 = string.digits
    s2 = string.ascii_lowercase
    s3 = string.ascii_uppercase
    l = randint(6,20)
    password = choice(s2) + choice(s1) + choice(s3)
    while len(password) < l:
        password += choice(s1+s2+s3)
    return password