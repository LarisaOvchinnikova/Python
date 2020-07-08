def coins(n):
    coins_in_row = 1
    amount = 0
    row = 0
    while amount < n:
        amount += coins_in_row
        coins_in_row += 1
        row += 1
    return row if amount == n else row-1

print(coins(2))
print(coins(3))
print(coins(5))
print(coins(8))
print(coins(10))