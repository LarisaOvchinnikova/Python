def is_balanced(s):
    count = 0
    for el in s:
        if el == "[":
            count += 1
        elif el == "]":
            count -=1
        if count < 0:
            return False
    return count == 0

s1 = "[[[]]]"  # valid
s2 = "[][][][]"  # valid
s3 = "]["  # invalid
s4 = "[[]][]]][["  # invalid
print(is_balanced(s1))
print(is_balanced(s2))
print(is_balanced(s3))
print(is_balanced(s4))