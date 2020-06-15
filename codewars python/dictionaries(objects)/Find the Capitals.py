def capital(capitals):
    res = []
    for el in capitals:
        if 'state' in el:
            res.append(f"The capital of {el['state']} is {el['capital']}")
        else:
            res.append(f"The capital of {el['country']} is {el['capital']}")
    return res
print()