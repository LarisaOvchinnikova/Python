text = "jack doe"
new_text = ""
for letter in text:
     if letter.lower() in "aeuio":
         new_text += letter.upper()
     else:
         new_text += letter

print(new_text)

