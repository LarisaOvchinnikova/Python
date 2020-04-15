def solve(a, b):
    if a == 0 and b != 0:
        return "no roots"
    elif a == 0 and b == 0:
        return "Infinity number of roots"
    else:
        x = -b / a
        return f"x = {round(x)}"
print(solve(1,2))
print(solve(0,3))
print(solve(0,0))
