# Strip the string of first 3 and last 3 characters
word2 = input("Enter word (length > 6): ")
if len(word2) < 7:
    print("Too short word for this task")
else:
    print(word2[3:-3])