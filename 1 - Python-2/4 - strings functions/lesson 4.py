print("123".isdigit())   #True
print("123.0".isdigit()) #False
print("123a0".isalnum())  #True
print("asd".isalpha())  #True
print("hello".center(10))
print("HELLO".isupper()) #True
print("123hello".islower()) #True

x = "hello"
for c in x:
    print(c)

for i in range(len(x)):
    print(x[i])

for i, char in enumerate(x):
    print(f"index {i} - {char}")

word = "hello world"
i = 0    
while i < len(word):
    print(word[i])
    i += 1