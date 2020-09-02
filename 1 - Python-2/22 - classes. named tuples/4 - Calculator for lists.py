# не работает!!!
def add_zeros(lst1, lst2):
    diff = abs(len(lst1) - len(lst2))
    print(diff)
    if len(lst1) > len(lst2):
        return lst1, lst2 + [0] * diff
    else:
        return lst1 + [0] * diff, lst2


class MathList(list):
    def __str__(self):
        value = super().__str__()
        return f"MathList({value})"

    def __add__(self, other):
        lst1, lst2 = add_zeros(self, other)
        print("after adding zeros:")
        print(lst1)
        print(lst2)
        res = [x + y for x, y in zip(lst1, lst2)]
        return res

    def __sub__(self, other):
        lst1, lst2 = add_zeros(self, other)
        return [x - y for x, y in zip(lst1, lst2)]


#list1 = MathList([10, 20, 30, 40])
#print('lst1:', list1)
#list2 = MathList([1, 2])
#print("list2:", list2)
#print("sum:", list1 + list2)
#print("diff:", list2 - list1)
list1 = MathList([1,2,3])
list2 = MathList([10,20, 30, 40, 50])
print(add_zeros(list1, list2))


help(str)
