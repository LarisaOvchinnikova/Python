#⭐Longest Sequence of Consecutive Zeroes

def longest_zero(s):
    arr = s.split('1')
    l = [len(word) for word in arr]
    return '0' * max(l)

print(longest_zero("01100001011000"))
print(longest_zero("100100100"))
print(longest_zero("1111"))