arr = [10,20,30]
for i in arr:
    i = i * 10
    print(i)   # no changing!
print(arr)

for i in range(len(arr)):
    arr[i] = arr[i] * 10
print(arr)