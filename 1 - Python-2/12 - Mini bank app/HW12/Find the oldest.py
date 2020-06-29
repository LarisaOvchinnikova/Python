def oldest(dct):
    m = max(dct.values())
    for key, value in dct.items():
        if value == m:
            return key


print(oldest({
  "Emma": 71,
  "Jack": 45,
  "Amy": 15,
  "Ben": 29
}))

print(oldest({
  "Max": 9,
  "Josh": 13,
  "Sam": 48,
  "Anne": 33
}))