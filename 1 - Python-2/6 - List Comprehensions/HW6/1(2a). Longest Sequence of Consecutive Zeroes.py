def longest_zero(s):
    x = s.split("1")
    lst = [len(el) for el in x]
    return "0" * max(lst)


print(longest_zero("01100001011000"))
print(longest_zero("100100100"))
print(longest_zero("11111"))