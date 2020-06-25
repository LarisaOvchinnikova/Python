# https://www.codewars.com/kata/5656b6906de340bd1b0000ac
def longest(s1, s2):
    return "".join(sorted(list(set(list(s1+s2)))))