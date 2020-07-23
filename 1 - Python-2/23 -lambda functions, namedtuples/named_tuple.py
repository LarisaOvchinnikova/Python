from collections import namedtuple
people = [("Lo", 23, "CA"), ("Bob", 34, "Fl"), ("Lara", 45, "CA")]

Person = namedtuple("Person", "name, age, address")
person_named = Person("Alice", 23, "FL")
print(person_named)
print(person_named.name)
new_person = Person("Lara", 30, "Fl")
print(new_person)
print(type(new_person)) # <class '__main__.Person'>
print(isinstance(new_person, tuple))  # True

old = ["Art", 49, "Fl"]
some_person = Person(old[0], old[1], old[2])
print(some_person)

# cпособ распаковки списков:
art = Person(*old)  #  * - разворачивание списка
print(art)

# ------------

people = [("Lo Pop", 53, "CA"), ("Bob Lop", 34, "Fl"), ("Lara Ov", 45, "CA")]
new_people = []
for new_one_tuple in people:
    new_one_nt = Person(*new_one_tuple)
    new_people.append(new_one_nt)

print(new_people)
# 2 case:
new_people1 = [Person(*record) for record in people]
print(new_people1)

def sort_by_age(element):
    return element.age  #element[1]

print(sorted(new_people, key=sort_by_age))

#======================
# сортировка по фамилии
names = ["Alice Moon", "Bob Key", "Lon Bool"]

def sort_by_lastname(element):
    return element.split()[1].lower()

print(sorted(names, key=sort_by_lastname))
#=====================================

def add(x, y):
    return x + y

print(add(1,2))

new_add = lambda x, y: x+y  #анонимная функция лямбда

print(new_add(1,2))
print(new_add)  # <function <lambda> at 0x01D8BA90>

print(sorted(new_people, key=lambda element:element.age))
print(sorted(new_people, key=lambda element:element.name.split()[1]))
# =======
dct = {
    "a": 10,
    "b": 5,
    "c": 15,
    "d": 23
}
print(dct.items())
print(sorted(dct.items(), key=lambda x: x[1]))

#==================
names = ["Alice Moon", "Bob Key", "Lon Bool"]
print(sorted(names, key=lambda el:len(el)))  # сортировка по длине

#------------
arr = [2,5,4,7,1,8]
print(sorted(arr, key=lambda el: el%2==0)) # [5, 7, 1, 2, 4, 8]

#сначала идут те, для которых условие false, затем те, для которых true
