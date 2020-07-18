def add_zeros(lst1, lst2):
    diff = abs(len(lst1) - len(lst2))
    if len(lst1) > len(lst2):
        return lst1, lst2 + [0] * diff
    else:
        return lst1 +[0] * diff, lst2
class MathList:
    def __init__(self, lst):
        self.lst = lst

    def __repr__(self):
        return f"MathList({self.lst})"

    def __add__(self, other):
        res = []
        arr1 = self.lst
        arr2 = other.lst
        arr1, arr2 = add_zeros(arr1, arr2)
        for i in range(len(arr1)):
            res.append(arr1[i] + arr2[i])
        return res

    def __sub__(self, other):
        arr1 = self.lst
        arr2 = other.lst
        arr1, arr2 = add_zeros(arr1, arr2)
        return [arr1[i] - arr2[i] for i in range(len(arr1))]

    def __mul__(self, other):
        arr1 = self.lst
        arr2 = other.lst
        arr1, arr2 = add_zeros(arr1, arr2)
        return [arr1[i] * arr2[i] for i in range(len(arr1))]

    def __floordiv__(self, other):
        arr1 = self.lst
        arr2 = other.lst
        arr1, arr2 = add_zeros(arr1, arr2)

        return [arr1[i] // arr2[i] if arr2[i] != 0 else 0 for i in range(len(arr1))]
        #return MathList(result)

lst1 = MathList([10,20,30])
print(lst1)
lst2 = MathList([10,0,30, 40])
print(lst2)
print(lst1 + lst2)
print(lst2 - lst1)
print(lst1 * lst2)
print(lst1//lst2)