x = [1,1,1,1,1]
x[0] = 10
print(x)  # array changed


s = "Hello"
s = s + "  user"
print(s) # new string
# s[0] = 'Y'  # not!!!!!!!!!!!!
print(s)


# -----
# tuple immutable sequence of objects --> array that can not change
x = (1,2,3,4)
print(x)

x = "Hi", "user"
print(x)  # --->("Hi", "user")

print(x[0])
x = (1,1,2,7,4,5,5)
print(x.index(7))    # 3

x = ('a', 'i', 'o')
print(x)
# ----------------------------------------
def add_nums(a,b):
    return a + b, a - b, a * b, a/b   #---->return tuple (6, -2, 8, 0.5)

print(add_nums(2,4))
# --------------------------------------
for i in (1,2,4,5,6):
    print(i)
# -------------------------------------
x = tuple(range(10))
print(x)

# ----------------------------
# Dictionaries ====> objects
x = {
    'name': "alice",
    'age': 12,
     1 : 12,
    (1,2): "t"
}
print(x)
print(x['name'])
x["password"] = 'qwerty'
print(x)
del x[1]  #delete key
print(x)
x.pop((1,2))  # delete key

print(x)

for i in x:
    print(i)

# -------------
s = "alice"
ob = {}
for i in s:
    if not i in ob:
        ob[i] = 1
    else:
        obj[i] += 1
print(ob)

# ---------
s = "hello my dear"
dct = {key:value for value, key in enumerate(s)}
print(dct)

