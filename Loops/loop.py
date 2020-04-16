# ----------------------------for ------------------------
colors = ["red", "green", "blue"]
for elem in colors:
    print(elem)
    elem = elem.capitalize()
    print(f"I like {elem}")

for i in range(len(colors)):
    print(i)
    print(colors[i])
    if i == 1:
        colors[i] = "white"


# ----------------------
nums = [10, 20, 5]
sum = 0
for el in nums:
    sum += el
print(sum)
# ----------------------
# 1,2,3,4...
# x = list(range(10))
for num in range(10):
    print(num)

# ===================

for num in range(5, 20, 2):
    print(num)
# ============
sum = 0
for i in range(15):
    if i % 3 == 0:
        print(i)
        sum += i
print(sum)
# -----------------
sum = 0
nums = [6, 4, 3, 0 -1, -5, -10]
for i in nums:
    if i > 0:
        sum  += i
    else:
        break;
print(sum)
for i in range(20, 10, -2):
    print(i)

print('---------------------')

# ---------------------------------------while----------
i = 0
while i < 5:
    print(i)
    i += 1
# ---------------
i = 0
while True:
    print("Hello")
    i += 1
    if i > 5:
        break
# ----------------
# while True:
#    name = input("What is your name?")
#    print("Hello " + name)
#    if name == "q":
#        break

# ----------------
#while True:
#    degrees = input("enter degrees in F")
#    if not degrees.isdigit():
 #       break
#    else:
#        c = (int(degrees) - 32) * 5 / 9
 #       print(c)

# ------------------
n = 2
power = 0
value = n
while value < 1000:
    power += 1
    value *= n
print(power, value)
# ------------------
n = 50
nums = [10, 4, 23, 6, 18, 27, 47]
# n1 + n2 === n? first pair those sum = 50
for el in nums:
    if (n - el) in nums:
        print(el, n - el)
        break
# -----------------continue---------------------------
for i in range(10):
    if i % 2 != 0:
        continue
    print(i)
