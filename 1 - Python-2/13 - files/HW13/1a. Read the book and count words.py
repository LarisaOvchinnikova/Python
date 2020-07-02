Не работает еще проверить

import string
file = open("harry potter and the sorcerer's stone.txt", encoding="utf-8-sig")
text = file.read()
text_new = ""
# for char in text:
#     if char not in string.punctuation:
#         text_new += char
text_new = [char for char in text if char not in string.punctuation]

text = text_new.split()

y = open("stopwords.txt", encoding="utf-8-sig")
stop_words = y.read()
stop_words = stop_words.lower().split()
file.close()
y.close()


#dct = {text.count(word): word for word in text if word not in stop_words}
text = [word for word in text if word not in stop_words]
counts = {}
for word in text:
    counts[word] = counts.get(word, 0) + 1

print(counts)

new_sorted = sorted([(value, key) for key, value in counts.items()], reverse = True)[:10]
sorted_counts = {key: value for value, ket in new_sorted}
print(sorted_counts)



