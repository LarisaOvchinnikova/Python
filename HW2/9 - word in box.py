word = input("Enter word: ")
width = int(input("Enter width of the box"))
if width < len(word):
    print("ERROR")
else:
    space = int((width - len(word))/2) - 1
    print("*" * width)
    print("*" + " "*space + word + " "*space + "*")
    print("*"*width)

# 2 case:

if width < len(word):
    print("ERROR")
else:
    space = int((width - len(word))/2) - 1
    print("*" * width)
    print("*" + word.center(width - 2) + "*")
    print("*"*width)
