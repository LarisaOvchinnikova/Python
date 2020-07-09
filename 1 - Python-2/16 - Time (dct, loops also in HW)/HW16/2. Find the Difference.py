def added_letter(s, t):
    s1 = sorted(s)
    t1 = sorted(t)
    for i in range(len(s1)):
        if t1[i] != s1[i]:
            return f"{t1[i]} is the letter that was added"
    return f"{t1[-1]} is the letter that was added"

# def added_letter(s, t):
#
#     return [char for i, char in enumerate(t) if not char in s]

print(added_letter("abcd", "abcde"))
print(added_letter("asde", "absde"))
print(added_letter("a", "aa"))
print(added_letter("aa", "aaz"))