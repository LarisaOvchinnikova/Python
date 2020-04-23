# Write a list comprehension for drunk_hello function
def drunk_hello(text):
    return "".join([letter.lower() if i % 2 != 0 else letter.upper() for i, letter in enumerate(text)])

text = "sky is blue"
print(drunk_hello(text))