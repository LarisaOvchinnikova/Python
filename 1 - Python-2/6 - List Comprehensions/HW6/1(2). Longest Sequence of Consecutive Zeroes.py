def longest_zero(s):
    x = s.split("1")
    return max(x)  # alphabet max,  0000>0


print(longest_zero("01100001011000"))
print(longest_zero("100100100"))
print(longest_zero("11111"))