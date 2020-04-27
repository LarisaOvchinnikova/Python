#⭐Longest Sequence of Consecutive Zeroes

def longest_zero(s):
    current = 0
    biggest = 0
    for num in s:
        if num == "0":
            current += 1
        if current > biggest:
            biggest = current
        if num == "1":
            current = 0
    return "0" * biggest


print(longest_zero("01100001011000"))
print(longest_zero("100100100"))
print(longest_zero("1111"))