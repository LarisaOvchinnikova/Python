def unique_in_order(s):
    res = []
    for i in range(len(s)):
        if s[i] != s[i-1] or i == 0:
            res.append(s[i])
    return res


def unique_in_order(s):
  return [s[i] for i in range(len(s)) if s[i] != s[i-1] or i == 0]

print(unique_in_order('AAAABBBCCDAABBB'))
