def duplicates(s):
    return "".join(["(" if s.count(char) == 1 else ")" for char in s.lower()])


print(duplicates("din"))     #   =>  "((("
print(duplicates("recede"))  #   =>  "()()()"
print(duplicates("Success")) #  =>  ")())())"
print(duplicates("(( @"))    #     =>  "))(("