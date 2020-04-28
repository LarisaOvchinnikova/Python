lst = [1,2,3,4,5,6]
if 6 in lst:     # проходит по всему списку
    print("yes")
print(lst[5])  # works quickly

lst = {1,2,3,4,5,6}
if 5 in lst:   #работает очень быстро без прохода циклом по сету
    print("yes")

print(hash("from"))