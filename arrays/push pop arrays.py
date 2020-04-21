arr = [0, 1, 2]
arr.append(10)  # push 1 to end --> [0,1,2,10]
print(arr)
arr.pop()
print(arr)     # delete last element ---> [0,1,2]
arr.remove(1)  # delete arr[1]  ---> [0,2]
print(arr)
arr.insert(0,20)  # like unshift ---> [20, 0,2]
print(arr)