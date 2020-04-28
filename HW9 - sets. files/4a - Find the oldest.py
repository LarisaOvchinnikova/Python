def oldest(dct):
    arr_values = list(dct.items())
    # arr_values.sort()
    arr = [(el[1], el[0]) for el in arr_values]
    print(arr_values)
    arr.sort(reverse=True)
    print(arr[0][1])
    return arr[0][1]


print(oldest({
  "Emma": 71,
  "Jack": 45,
  "Amy": 15,
  "Ben": 29
})
)