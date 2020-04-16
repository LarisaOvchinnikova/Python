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
