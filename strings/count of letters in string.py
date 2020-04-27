text = "sky is blue"
print(text.count("s"))  # count of letters s in text
text = "sky is blue and bright"
print(text.count(" "))
# count every symbol in string:
for letter in text:
    print(letter, text.count(letter))
