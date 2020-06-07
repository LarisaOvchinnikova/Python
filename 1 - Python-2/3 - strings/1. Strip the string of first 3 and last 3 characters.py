word = input("Enter text (length > 6): ")
if len(word) < 7:
    print("Too short word for this task")
else:
    print(word[3:-3])