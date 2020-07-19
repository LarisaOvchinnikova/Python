def add_zeros(arr1, arr2):
    d = abs(len(arr2) - len(arr1))
    if len(arr1) < len(arr2):
        return arr1 + [0] * d, arr2
    else:
        return arr1, arr2 + [0] * d


class MathList:
    def __init__(self, lst):
        self.lst = lst

    def __repr__(self):
        return f"MathList  {self.lst}"

    def __add__(self, other):
        arr1 = self.lst
        arr2 = other.lst
        if len(arr1) != len(arr2):
            arr1, arr2 = add_zeros(arr1, arr2)
        return [arr1[i] + arr2[i] for i in range(len(arr1))]

    def __sub__(self, other):
        arr1 = self.lst
        arr2 = other.lst
        if len(arr1) != len(arr2):
            arr1, arr2 = add_zeros(arr1, arr2)
        return [arr1[i] - arr2[i] for i in range(len(arr1))]

    def __mul__(self, other):
        arr1 = self.lst
        arr2 = other.lst
        if len(arr1) != len(arr2):
            arr1, arr2 = add_zeros(arr1, arr2)
        return [arr1[i] * arr2[i] for i in range(len(arr1))]

    def __floordiv__(self, other):
        arr1 = self.lst
        arr2 = other.lst
        if len(arr1) != len(arr2):
            arr1, arr2 = add_zeros(arr1, arr2)

        try:
            return [arr1[i] // arr2[i] for i in range(len(arr1))]
        except ZeroDivisionError:
            return [arr1[i] // arr2[i] if arr2[i] != 0 else 0 for i in range(len(arr1))]


list1 = MathList([30, 40, 1, 3])
list2 = MathList([10, 20])
print(list1)
print(list2)

print(f"Add: {list1 + list2}")
print(f"Sub: {list1 - list2}")
print(f"Mult: {list1 * list2}")
print(f"FloorDiv: {list1 // list2}")