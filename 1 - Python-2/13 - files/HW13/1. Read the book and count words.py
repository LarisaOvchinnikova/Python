import string
x = open("harry potter and the sorcerer's stone.txt", encoding="utf-8-sig")
text = x.read()
text_new = ""
for char in text:
    if not char in string.punctuation:
        text_new += char
text = text_new.lower().split()

y = open("stopwords.txt", encoding="utf-8-sig")
stop_words = y.read()
stop_words = stop_words.lower().split()

dct = {text.count(word): word for word in text if not word in stop_words}
arr = list(dct.items())
arr.sort(reverse=True)

dct = {word[1]: word[0] for word in arr[:20]}
print(dct)
x.close()
y.close()

