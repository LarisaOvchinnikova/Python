# X and Y Coordinates
def convert_cartesian(x, y):
    lst = []
    for i in range(len(x)):
        lst.append((x[i], y[i]))
    return lst

print(convert_cartesian([1, 5, 3, 3, 4], [5, 8, 9, 1, 0]) )
# -----------
x = [1,5,3,3,4]
y = [5,8,9,1,0]
lst = [(el, el1) for el in x  for el1 in y]
print(lst)