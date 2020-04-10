a = int(input('Input number a: '))
b = int(input('Input number b: '))
c = int(input('Input number c: '))
d = b ** 2 - 4 * a * c
if d > 0:
    x1 = (-b + d ** 0.5) / (2 * a)
    x2 = (-b - d ** 0.5) / (2 * a)
    print('x1 = ', round(x1, 2), 'x2 = ', round(x2, 2))
elif d == 0:
    x = -b / ( 2* a)
    print('x = ', round(x, 2))
else:
    print('No roots')
