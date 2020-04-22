# Count Palindrome Numbers in a Range

def isPalindrome(n):
    rev = ''
    n = str(n)
    for i in n:
       rev = i + rev
    return n == rev

def count_palindromes(n, m):
    count = 0
    for i in range(n, m + 1):
        if isPalindrome(i):
            count += 1
    return count

print(count_palindromes(1, 10))    # ---> 9
print(count_palindromes(555, 556)) # ---> 1
print(count_palindromes(878, 898)) # ---> 3