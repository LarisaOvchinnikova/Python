def is_balanced(s):
    count = 0
    for i in s:
        if i == "[":
            count += 1
        elif i == "]":
            count -= 1
        if count < 0:
            return False
    return True
print(is_balanced("[[[]]]"))
print(is_balanced("[][][][]"))
print(is_balanced("]["))
print(is_balanced("[[]][]]][["))
