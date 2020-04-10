# Insert second string in the middle of the first string
first = input("input string")
second = input("input word to insert in string")
i = int(len(first)/2)
print(f"New string: {first[0:i]+second+first[i:]}")
