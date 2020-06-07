first = input("Enter the first string: ")
second = input("Enter the second string: ")
i = len(first) // 2
print(f"New string: {first[0:i]+second+first[i:]}")