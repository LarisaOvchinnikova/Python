def common_prefix(arr):
    start = 0
    end = 1
    common_pr = ""

    for j in range(len(arr[0])):
        prefix = arr[0][start: end]
        for el in arr:
            if not el.startswith(prefix):
                return common_pr
            else:
                continue
        common_pr = prefix
        end += 1
    return common_pr
print(common_prefix(["flower","flow","flight"]))
print(common_prefix(["dog","racecar","car"]))
print(common_prefix(['monkey', 'monday']))