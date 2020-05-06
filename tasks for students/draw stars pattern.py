# *****
# *****
# *****
for i in range(3):
    print("*" * 5)
# -----------------------------------------
# triangle
# *
# **
# ***
# ****
# *****
for i in range(5):
    print("*" * i)

# ------------------------------------------
# ****
# ***
# **
# *
# triangle
for i in range(5, 0, -1):
    print("*" * i)

# ----------------------------------
for i in range(1, 9, 2):
    print(("*"*i).center(10))

for i in range(7, 0, -2):
    print(("*" * i).center(10))

for i in range(10):
    print(str(i) * i)

for i in range(7):
    print(("*"*i).rjust(10))
