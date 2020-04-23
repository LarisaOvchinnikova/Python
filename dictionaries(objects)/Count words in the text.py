# Count words in the text
def countWords(text):
    obj = {}
    text = text.lower().split()
    for word in text:
#        if not word in obj:
#           obj[word] = 1
#       else:
#          obj[word] += 1
        obj[word] = obj.get(word, 0) + 1
    return obj

print(countWords("Roses are red violets are blue roses are nice"))
# obj["are"]  ---> obj.get("are")
