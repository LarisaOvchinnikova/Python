import string
x = open("harry potter and the sorcerer's stone.txt", encoding="utf-8-sig")
text = x.read()  # все одной строкой через \n
text_new = ""
for char in text:
    if not char in string.punctuation:
        text_new += char
text = text_new.lower().split()
print(text)
y = open("stopwords.txt", encoding="utf-8-sig")
stop_words = y.read()
stop_words = stop_words.lower().split()
print(stop_words)


dct = {text.count(word): word for word in text if not word in stop_words}
print(dct)
arr = list(dct.items())
arr.sort(reverse=True)
dct = {word: count for count, word in enumerate(arr)}
print(dict(arr[:10]))
x.close()
y.close()