def solve(a,b):
    if a == 0 or b == 0:
        print(f"#1 {a},{b}")
        return [a, b]
    elif a >= 2*b:
        print(f"#2 {a},{b}")
        a = a - 2*b
        solve(a, b)
    elif b >= 2*a:
        print(f"#3 {a},{b}")
        b = b - 2*a
        solve(a, b)
    else:
        print(f"#4 {a},{b}")
        return [a, b]


print(solve(6, 19))