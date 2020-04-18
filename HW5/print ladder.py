n = 5
for i in range(n):
    print('*' * (i + 1))
for i in range(n):
    print('*' * ( n - i ))
print('-----------------')
for i in range(n, 0, -1):
    print('*' * i)
