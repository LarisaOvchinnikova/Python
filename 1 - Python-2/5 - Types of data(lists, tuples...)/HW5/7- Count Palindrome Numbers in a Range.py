def count_palindromes(n, m):
    res = []
    for i in range(n, m+1):
        lst = list(str(i))
        reverse = lst[::-1]
        if "".join(lst) == "".join(reverse):
            res.append(i)
    return res


print(count_palindromes(1, 10))
print(count_palindromes(8, 34))
print(count_palindromes(1500, 1552))