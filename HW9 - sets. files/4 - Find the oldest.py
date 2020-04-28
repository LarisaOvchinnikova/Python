def oldest(dct):
    arr_values = list(dct.values())
    print(arr_values)
    arr_values.sort(reverse=True)
    m = arr_values[0]

    return m

print(oldest({
  "Emma": 71,
  "Jack": 45,
  "Amy": 15,
  "Ben": 29
})
)