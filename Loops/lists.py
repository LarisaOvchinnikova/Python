names = ["Ann", "Amelia", "Artem"]
firstLetters = []
for i in names:
    firstLetters.append(i)
    firstLetters.append(i[0])
print(firstLetters)
# -------
nums = [6,2,3,5,10,29]
total = []
n = 8
for number in nums:
    if n - number in nums:
        lst = [n-number, number]
        lst.sort()
        if not lst in total:
          total.append(lst)


print(total)
