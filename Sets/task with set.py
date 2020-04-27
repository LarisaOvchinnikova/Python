y = list(range(1,11))
print(y)
x = [1,2,3,10,5,4,7,6,8]
print(x)
# найти какого элемента из y не хватает в х
setY = set(y)
setX = set(x)
print(setY - setX)  # --> 9
